# q1
def music_func(mtype="CLassic Rock", mgroup="The Beatles", vocal="Freddie Mercury"):
    print(f"The best kind of music is {mtype}")
    print(f"The best music group is {mgroup}")
    print(f"The best lead vocalist is {vocal}")


def main():
    # DO NOT CHANGE THE MAIN FUNCTION
    music, group, singer = input().split(',')
    music_func(music, group, singer)
    print()
    music_func()


if __name__ == "__main__":
    main()

# q2
def sort_list(int_list):
    int_list.sort()

def main():
    #loop to accept integers until an empty string is entered goes here
    num_str = input()
    a_list = []
    while not num_str == "":
        a_list.append(int(num_str))
        num_str = input()
    ######Do not modify this part######
    print(a_list)
    sort_list(a_list)
    print(a_list)
    ######Do not modify this part######
    ######main() ends here
if __name__ == "__main__":
    main()

# q3
import string

def build_wordlist(fp):
    lines = fp.readlines()
    fp.close()
    wordlist = []
    for line in lines:
        words = line.strip().strip(string.punctuation).split(" ")
        for word in words:
            wordlist.append(word)
    return wordlist

def find_unique(wordlist):
    return list(set(wordlist))

def main():
    #DO NOT CHANGE THIS FUNCTION
    filename = input("Enter a file name:")
    infile = open(filename, 'r')
    word_list = build_wordlist(infile)
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print()
    print(new_wordlist)

if __name__ == "__main__":
    main()

# q4
def game_of_eights(game_list):
    val = False
    for i in range(len(game_list) - 1):
        num = game_list[i]
        add_num = game_list[i + 1]
        if not (num.isdigit() and add_num.isdigit()):
            return "Error. Please enter only integers."
        if num == add_num and num == "8":
            val = True
    return val
def main():
    a_list = input("Enter elements of list separated by commas: \n").split(',')
    result = game_of_eights(a_list)
    print(result)

if __name__ == "__main__":
    main()