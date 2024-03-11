import string
from operator import itemgetter


def add_word(word_map, word: str):
    """Adds word argument to the given word map"""
    # If word is not in given word map, create the key and set
    # the value (occurences) to 0
    word = word.lower()
    if word not in word_map:
        word_map[word] = 0

    # Increase occurence of given word by 1
    word_map[word] += 1


def build_map(in_file, word_map):
    """Builds the map given a file and a word map. Map contents are each word within the file stripped of punctuation and newlines"""
    # Iterates for each line within the file
    for line in in_file:

        # Splits each line by whitespace to create a list of words
        word_list = line.split()

        for word in word_list:
            # Strips each word of newlines and punctuation and adds word to word_map
            word = word.strip().strip(string.punctuation)
            if not word:
                continue
            add_word(word_map, word)


def display_map(word_map):
    """Given word map, sorts each word map by frequency and prints it out with formatting"""
    # Sort by word in ascending order
    freq_list = sorted(word_map.items(), key=itemgetter(0))
    # Then sort by frequency in descending order
    freq_list.sort(key=itemgetter(1), reverse=True)

    print("\n{:15s}{:5s}".format("Word", "Count"))
    print("-" * 20)
    for item in freq_list:
        print("{:15s}{:>5d}".format(item[0], item[1]))


def open_file():
    file_exists = False

    while not file_exists:
        try:
            file_name = input("Enter file name: ")
            fp = open(file_name, "r")
            return fp

        except FileNotFoundError:
            print("\n*** unable to open file ***\n")


def main():
    word_map = {}
    in_file = open_file()
    print()
    build_map(in_file, word_map)
    display_map(word_map)
    in_file.close()


main()