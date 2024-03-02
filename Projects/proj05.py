##################################################
# Computer Project #5
#
# Uses a csv file to analyze Yu-Gi-Oh! card data
# Outputs the card data, search results, and decklist
# Also can use ydk files to display the decklist
#
##################################################

import csv
from operator import itemgetter
from typing import TextIO, List

MENU = "\nYu-Gi-Oh! Card Data Analysis" \
           "\n1) Check All Cards" \
           "\n2) Search Cards" \
           "\n3) View Decklist" \
           "\n4) Exit" \
           "\nEnter option: "

CATEGORIES = ["id", "name", "type", "desc", "race", "archetype", "card price"]

def open_file(prompt_str : str) -> TextIO:
    """Prompts the user for a file name and returns the file pointer."""
    while True:
        file_loc = input(prompt_str)
        try:
            fp = open(file_loc, "r", encoding = " utf-8")
            break
        except FileNotFoundError:
            # If the file is not found, the user is prompted to try again
            print("\nFile not Found. Please try again!")
    return fp

def read_card_data(fp: TextIO) -> List[tuple]:
    """Reads the card data from the file and returns a list of tuples ordered by price and name."""
    lines = csv.reader(fp)
    card_data = []
    next(lines)
    for line in lines:
        card_data.append((line[0], line[1][:45], line[2], line[3], line[4], line[5], float(line[6])))
    card_data.sort(key=itemgetter(6, 1))
    return card_data

def read_decklist(fp : TextIO, card_data: List[tuple]) -> List[tuple]:
    """Reads the decklist from a ydk file, finds the matching ids and returns a list of tuples containing cards ordered by price and name."""
    ids_list = [line.strip() for line in fp.readlines()]
    matched_cards = []
    for card_ids in ids_list:
        for card in card_data:
            if card_ids == card[0]:
                matched_cards.append(card)
    matched_cards.sort(key=itemgetter(6, 1))
    return matched_cards

def search_cards(card_data:List[tuple], query: str, category_index: int) -> List[tuple]:
    """Searches the card data for the query in the specified category and returns a list of tuples containing cards ordered by price and name."""
    filtered_cards = [card for card in card_data if query in card[category_index]]
    filtered_cards.sort(key=itemgetter(6, 1))
    return filtered_cards

def compute_stats(card_data: List[tuple]) -> tuple[List[tuple], float, List[tuple], float, List[tuple], float]:
    """Computes the minimum, maximum, and median prices and returns the corresponding cards and prices. Ordered by name."""

    # Initializes the minimum, maximum, and median prices and cards
    min_price, max_price, med_price = float('inf'), -float('inf'), 0.0
    min_cards, max_cards, med_cards = [], [], []
    card_data.sort(key=itemgetter(6))

    # Loops through the card data and finds the minimum and maximum prices and cards
    for i in range(len(card_data)):
        card = card_data[i]
        price = float(card[6])

        if price < min_price:
            min_price, min_cards = price, [card]
        elif price == min_price:
            min_cards.append(card)

        if price > max_price:
            max_price, max_cards = price, [card]
        elif price == max_price:
            max_cards.append(card)

    # Finds the median price by finding the middle index and checking if the length is even or odd
    middle = len(card_data) // 2
    if len(card_data) % 2 == 0:
        med_price = max(card_data[middle][6], card_data[middle-1][6])
    else:
        med_price = card_data[middle][6]
    # Finds the cards with the median price
    med_cards = [card for card in card_data if card[6] == med_price]

    # Sorts the cards by name
    med_cards.sort(key=itemgetter(1))
    min_cards.sort(key=itemgetter(1))
    max_cards.sort(key=itemgetter(1))
    return min_cards, min_price, max_cards, max_price, med_cards, med_price

def display_data(card_data : List[tuple]):
    """Displays the card data in a formatted table."""
    print("{:50}{:30}{:20}{:40}{:12}".format("Name", "Type", "Race","Archetype", "TCGPlayer"))
    total = 0.0
    # Loops through the card data and prints
    for card in card_data:
        print("{:50}{:30}{:20}{:40}{:12,.2f}".format(card[1], card[2], card[4], card[5], card[6]))
        total += card[6]
    print("\n{:50}{:30}{:20}{:40}{:12,.2f}".format("Totals", "", "", "", total))

def display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price):
    """Displays the minimum, maximum, and median prices and the corresponding cards."""
    print("\nThe price of the least expensive card(s) is {:,.2f}".format(min_price))
    for card in min_cards:
        print(f"\t{card[1]}")
    print("\nThe price of the most expensive card(s) is {:,.2f}".format(max_price))
    for card in max_cards:
        print(f"\t{card[1]}")
    print("\nThe price of the median card(s) is {:,.2f}".format(med_price))
    for card in med_cards:
        print(f"\t{card[1]}")

def main():
    # Prompts the user for the file name and reads the card data
    fp = open_file("\nEnter cards file name: ")
    card_data = read_card_data(fp)

    # Closes the file
    fp.close()
    # Loops until the user decides to exit
    while True:
        # Prompts the user for an option and performs the corresponding action
        user_input = input(MENU)
        match user_input:
            # Option 1 - Check All Cards
            case "1":
                # Sorts the card data by price and displays the first 50 cards
                card_data.sort(key=itemgetter(6))
                print("\nThere are {} cards in the dataset.".format(len(card_data)))
                limited_data = card_data[:50]
                display_data(limited_data)
                min_cards, min_price, max_cards, max_price, med_cards, med_price = compute_stats(card_data)
                display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price)
            # Option 2 - Search Cards
            case "2":
                # Prompts the user for a query and category and displays the search results
                query = input("\nEnter query: ")
                category = input("\nEnter category to search: ").lower()
                while True:
                    # Loops until the user enters a valid category
                    if category not in CATEGORIES:
                        print("\nIncorrect category was selected!")
                        category = input("\nEnter category to search: ").lower()
                        continue
                    break
                # Finds the category index and filters the card data
                category_id = CATEGORIES.index(category)
                filtered_data = search_cards(card_data, query, category_id)
                print("\nSearch results")
                # Displays the search results and the corresponding statistics
                if len(filtered_data) == 0:
                    # If there are no cards, the user is notified
                    print(f"\nThere are no cards with '{query}' in the '{category}' category.")
                else:
                    # If there are cards, the user is notified and the cards are displayed
                    print(f"\nThere are {len(filtered_data)} cards with '{query}' in the '{category}' category.")
                    display_data(filtered_data)
                    min_cards, min_price, max_cards, max_price, med_cards, med_price = compute_stats(filtered_data)
                    display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price)
            # Option 3 - View Decklist
            case "3":
                # Prompts the user for a decklist filename and displays the decklist
                decklist_filename = input("\nEnter decklist filename: ")
                fp = open(decklist_filename, "r", encoding = " utf-8")
                # Reads the decklist and displays the search results and the corresponding statistics
                filtered_data = read_decklist(fp, card_data)
                fp.close()
                print("\nSearch results")
                display_data(filtered_data)
                min_cards, min_price, max_cards, max_price, med_cards, med_price = compute_stats(filtered_data)
                display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price)
            # Option 4 - Exit
            case "4":
                # Exits the program
                print("\nThanks for your support in Yu-Gi-Oh! TCG")
                exit(0)
            # Invalid Option
            case _:
                print("Invalid option. Please try again!")

if __name__ == "__main__":
    main()

