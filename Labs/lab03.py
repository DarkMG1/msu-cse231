VOWELS = "aeiou"
word = input("Enter a word ('quit' to quit): \n").lower()
while word != "quit":
    while len(word) == 0:
        print("Can't convert an empty string. Try again.")
        word = input("Enter a word ('quit' to quit): \n").lower()
    if word[0] in VOWELS:
        print(word + "way")
    else:
        consonants = ""
        i = 0
        while word[i] not in VOWELS:
            consonants += word[i]
            i += 1
            if i == len(word):
                break
        word = word[i:]
        print(word + consonants + "ay")
    word = input("Enter a word ('quit' to quit): \n").lower()