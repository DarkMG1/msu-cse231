################################################################################
# Computer Project #7
#
# crossword.py
#
# This file contains the implementation of the Crossword and Clue classes. The Crossword class
# represents a crossword puzzle and contains methods to interact with the puzzle. The Clue class
# represents a clue in the crossword puzzle and contains methods to interact with the clue.
#
################################################################################

import csv

CROSSWORD_DIMENSION = 5

GUESS_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"


class Clue:
    def __init__(self, indices: tuple, down_across: str, answer: str, clue: str):
        """
        Puzzle clue constructor
        :param indices: row,column indices of the first letter of the answer
        :param down_across: A for across, D for down
        :param answer: The answer to the clue
        :param clue: The clue description
        """
        self.indices = indices
        self.down_across = down_across
        self.answer = answer
        self.clue = clue

    def __str__(self):
        """
        Return a representation of the clue (does not include the answer)
        :return: String representation of the clue
        """
        return f"{self.indices} {'Across' if self.down_across == 'A' else 'Down'}: {self.clue}"

    def __repr__(self):
        """
        Return a representation of the clue including the answer
        :return: String representation of the clue
        """
        return str(self) + f" --- {self.answer}"

    def __lt__(self, other):
        """
        Returns true if self should come before other in order. Across clues come first,
        and within each group clues are sorted by row index then column index
        :param other: Clue object being compared to self
        :return: True if self comes before other, False otherwise
        """
        return ((self.down_across,) + self.indices) < ((other.down_across,) + other.indices)


class Crossword:
    def __init__(self, filename):
        """
        Crossword constructor
        :param filename: Name of the csv file to load from. If a file with
        this name cannot be found, a FileNotFoundError will be raised
        """
        self.clues = dict()
        self.board = [['■' for _ in range(CROSSWORD_DIMENSION)] for __ in range(CROSSWORD_DIMENSION)]
        self._load(filename)

    def _load(self, filename):
        """
        Load a crossword puzzle from a csv file
        :param filename: Name of the csv file to load from
        """
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                indices = tuple(map(int, (row['Row Index'], row['Column Index'])))
                down_across, answer = row['Down/Across'], row['Answer']
                clue_description = row['Clue']
                clue = Clue(indices, down_across, answer, clue_description)

                key = indices + (down_across,)
                self.clues[key] = clue

                i = 0
                while i < len(answer):
                    if down_across == 'A':
                        self.board[indices[0]][indices[1] + i] = '_'
                    else:
                        self.board[indices[0] + i][indices[1]] = '_'
                    i += 1

    def __str__(self):
        """
        Return a string representation of the crossword puzzle,
        where the first row and column are labeled with indices
        :return: String representation of the crossword puzzle
        """
        board_str = '     ' + '    '.join([str(i) for i in range(CROSSWORD_DIMENSION)])
        board_str += "\n  |" + "-"*(6*CROSSWORD_DIMENSION - 3) + '\n'
        for i in range(CROSSWORD_DIMENSION):
            board_str += f"{i} |"
            for j in range(CROSSWORD_DIMENSION):
                board_str += f"  {self.board[i][j]}  "
            board_str += '\n'

        return board_str

    def __repr__(self):
        """
        Return a string representation of the crossword puzzle,
        where the first row and column are labeled with indices
        :return: String representation of the crossword puzzle
        """
        return str(self)

    def change_guess(self, clue: Clue, new_guess: str) -> None:
        """
        Updates the crossword puzzle with a new guess for a given clue
        :param clue:  Represents the clue for which the user is making a guess
        :param new_guess: User's new guess for the answer to the clue
        """
        counter = 0
        # Check if the guess length matches the length of the clue
        if len(new_guess) != len(clue.answer):
            raise RuntimeError("Guess length does not match the length of the clue.\n")

        # Check if the guess contains invalid characters
        while counter < len(new_guess):
            if new_guess[counter] not in GUESS_CHARS:
                # raise an error if the guess contains invalid characters
                raise RuntimeError("Guess contains invalid characters.\n")
            counter += 1

        # Update the board with the new guess
        row_index, col_index = clue.indices
        current_letter = 0
        while current_letter < len(new_guess):
            if clue.down_across == "A":
                self.board[row_index][col_index + current_letter] = new_guess[current_letter]
            else:
                self.board[row_index + current_letter][col_index] = new_guess[current_letter]
            current_letter += 1

    def reveal_answer(self, clue: Clue) -> None:
        """
        Automatically fill in the ocrrect answer for a specific clue ont he corssword puzzle board.
        :param clue: Represents the puzzle clue for which the answer is to be revealed
        :return: None
        """
        row_index, col_index = clue.indices
        current_letter = 0
        # Update the board with the correct answer
        while current_letter < len(clue.answer):
            if clue.down_across == "A":
                self.board[row_index][col_index + current_letter] = clue.answer[current_letter]
            else:
                self.board[row_index + current_letter][col_index] = clue.answer[current_letter]
            current_letter += 1

    def find_wrong_letter(self, clue: Clue) -> int:  # fill out the parameters
        """
        Finds the first instance where the user's guess diverges from the correct answer.
        :param clue: Clue for which the method is trying to find an incorrect guess
        :return: int: The index of the first incorrect guess
        """
        row_index, col_index = clue.indices
        current_letter = 0
        while current_letter < len(clue.answer):
            if clue.down_across == "A":
                if self.board[row_index][col_index + current_letter] != clue.answer[current_letter]:
                    return current_letter
            else:
                if self.board[row_index + current_letter][col_index] != clue.answer[current_letter]:
                    return current_letter
            current_letter += 1
        return -1

    def is_solved(self) -> bool:
        """
        Check if the crossword puzzle has been solved
        :return: bool: True if the puzzle has been solved, False otherwise
        """
        for key in self.clues:
            if self.find_wrong_letter(self.clues[key]) != -1:
                return False
        return True
