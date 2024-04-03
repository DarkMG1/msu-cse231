################################################################################
# Computer Project #7
#
# proj07.py
#
# This program is a crossword puzzle game that allows the user to interact with the crossword puzzle
# by making guesses, revealing answers, and getting hints. The user can also display the clues for the
# puzzle, restart the game, or quit the program. The program reads the crossword puzzle from a file and
# processes the data according to the user's menu choice.
#
################################################################################

from proj7_crossword import Crossword, Clue
import sys


HELP_MENU = "\nCrossword Puzzler -- Press H at any time to bring up this menu" \
                "\nC n - Display n of the current puzzle's down and across clues" \
                "\nG i j A/D - Make a guess for the clue starting at row i, column j" \
                "\nR i j A/D - Reveal the answer for the clue starting at row i, column j" \
                "\nT i j A/D - Gives a hint (first wrong letter) for the clue starting at row i, column j" \
                "\nH - Display the menu" \
                "\nS - Restart the game" \
                "\nQ - Quit the program"

# def input( prompt=None ):
#     """
#         DO NOT MODIFY: Uncomment this function when submitting to Codio
#         or when using the run_file.py to test your code.
#         This function is needed for testing in Codio to echo the input to the output
#         Function to get user input from the standard input (stdin) with an optional prompt.
#         Args:
#             prompt (str, optional): A prompt to display before waiting for input. Defaults to None.
#         Returns:
#             str: The user input received from stdin.
#     """
#
#     if prompt:
#         print( prompt, end="" )
#     aaa_str = sys.stdin.readline()
#     aaa_str = aaa_str.rstrip( "\n" )
#     print( aaa_str )
#     return aaa_str


def open_puzzle() -> Crossword:
    """
    Prompts user to enter the name of the puzzle file to load in the crossword object.
    :return: Crossword object
    """
    file_name = ""
    crossword = None
    while True:
        file_name = input("Enter the filename of the puzzle you want to play: ")
        try:
            crossword = Crossword(file_name)
            break
        except FileNotFoundError:
            print("No puzzle found with that filename. Try Again.\n")
    return crossword

def display_clues(crossword: Crossword, num_clues: int = 0) -> None:
    """
    Displays the first num_clues clues for the puzzle.
    :param crossword: Crossword object
    :param num_clues: Integer representing the number of clues to display. Default is 0 which means all clues are displayed.
    """
    if num_clues == 0:
        num_clues = len(crossword.clues)

    # Display the first num_clues clues
    counter = 0
    print("Across")
    for key, items in crossword.clues.items():
        # Break if the number of clues displayed is equal to the number of clues requested
        if counter == num_clues:
            break
        # Display the across clues
        if key[2] == "A":
            print(items)
            counter += 1

    print("\nDown")
    counter  = 0
    for key, items in crossword.clues.items():
        # Break if the number of clues displayed is equal to the number of clues requested
        if counter == num_clues:
            break
        # Display the down clues
        if key[2] == "D":
            print(items)
            counter += 1

def locate_clue(crossword: Crossword, row_index: int, col_index: int, direction: str) -> Clue | None:
    """
    Locates a clue in the crossword object based on the row, column, and direction provided.
    :param crossword: Crossword object
    :param row_index: Integer representing the row index of the clue
    :param col_index: Integer representing the column index of the clue
    :param direction: String representing the direction of the clue (A for across, D for down)
    :return: Clue object
    """
    for key, items in crossword.clues.items():
        # Return the clue if the key matches the row, column, and direction
        if key == (row_index, col_index, direction):
            return items
    return None
def validate_inputs(crossword: Crossword, user_input: str) -> tuple | None:
    """
    Validates user inputs based on different command options within the context of interacting with the crossword puzzle.
    Processes command inputs and ensures they are appropriate for the specified command before proceeding with game actions.
    :param crossword: Crossword object
    :param user_input: String representing the space-seperated arguments input by the user
    :return: Tuple containing the command and its corresponding arguments. Returns None if the input is invalid.
    """
    user_input = user_input.split()

    if user_input[0] == "C":
        if len(user_input) != 2:
            return None
        if not user_input[1].isdigit():
            return None
        user_int = int(user_input[1])
        if user_int < 0:
            return None
        return "C", user_int
    elif user_input[0] in ["H", "S", "Q"]:
        if len(user_input) != 1:
            return None
        return user_input[0], None
    elif user_input[0] in ["G", "R", "T"]:
        if len(user_input) != 4:
            return None
        if not user_input[1].isdigit() or not user_input[2].isdigit():
            return None
        if user_input[3] not in ["A", "D"]:
            return None
        row_index = int(user_input[1])
        col_index = int(user_input[2])
        if row_index < 0 or col_index < 0:
            return None
        # Check if the clue exists
        for key in crossword.clues.keys():
            if key[:2] == (row_index, col_index):
                return user_input[0], row_index, col_index, user_input[3]
        return None


def main():
    # Load the crossword puzzle
    crossword = open_puzzle()
    display_clues(crossword)
    # Display the crossword puzzle
    print(crossword)
    # Display the help menu
    print(HELP_MENU)

    # Main game loop
    while True:
        # Get user input
        user_input = input("\nEnter option: ")

        # Validate user input
        command = validate_inputs(crossword, user_input)

        # Process user input
        if not command:
            print("Invalid option/arguments. Type 'H' for help.")
            continue
        if command[0] == "C":
            # Display the first n clues
            display_clues(crossword, command[1])
        elif command[0] == "G":

            # Make a guess for the clue
            clue = locate_clue(crossword, command[1], command[2], command[3])

            # Check if the clue exists
            while not clue:
                print("Invalid option/arguments. Type 'H' for help.")
                user_input = input("\nEnter option: ")
                clue = locate_clue(crossword, command[1], command[2], command[3])

            # Change the guess
            while True:
                try:
                    guess = input("Enter your guess (use _ for blanks): ").upper()
                    crossword.change_guess(clue, guess)
                    break
                except RuntimeError as e:
                    # Display error message
                    print(e)
            # Display the crossword puzzle
            print(crossword)

            # Check if the puzzle is solved
            if crossword.is_solved():
                print("\nPuzzle solved! Congratulations!")
                break
        elif command[0] == "R":
            # Reveal the answer for the clue

            # Locate the clue
            clue = locate_clue(crossword, command[1], command[2], command[3])

            # Check if the clue exists
            while not clue:
                print("Invalid option/arguments. Type 'H' for help.")
                user_input = input("\nEnter option: ")
                clue = locate_clue(crossword, command[1], command[2], command[3])

            # Reveal the answer
            crossword.reveal_answer(clue)

            # Display the crossword puzzle
            print(crossword)

            # Check if the puzzle is solved
            if crossword.is_solved():
                print("\nPuzzle solved! Congratulations!")
                break
        elif command[0] == "T":
            # Get a hint for the clue

            # Locate the clue
            clue = locate_clue(crossword, command[1], command[2], command[3])

            # Check if the clue exists
            while not clue:
                print("Invalid option/arguments. Type 'H' for help.")
                user_input = input("\nEnter option: ")
                clue = locate_clue(crossword, command[1], command[2], command[3])

            # Find the first wrong letter
            incorrect_index = crossword.find_wrong_letter(clue)

            # Display the hint
            if incorrect_index == -1:
                print("This clue is already correct!")
            else:
                print("Letter {} is wrong, it should be {}".format(incorrect_index + 1, clue.answer[incorrect_index]))
        elif command[0] == "H":
            # Display the help menu
            print(HELP_MENU)
        elif command[0] == "S":
            # Restart the game
            crossword = open_puzzle()
            display_clues(crossword)
            print(crossword)
            print(HELP_MENU)
        elif command[0] == "Q":
            # Quit the program
            break
    return


if __name__ == "__main__":
    main()
