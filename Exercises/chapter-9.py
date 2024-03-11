# q1
from operator import itemgetter

repeat = True
the_dict = []

while repeat:
  inside = False
  name = input("\nName: ")
  number = input("\nNumber: ")
  for data in the_dict:
    if data[0] == name:
      inside = True
  if not inside:
    data = (name, number)
    the_dict.append(data)
  repeat_str = input('\nMore data (y/n)? ')
  if repeat_str == "y":
    continue
  repeat = False

the_dict.sort(key=itemgetter(0))
print("\nThe sorted data:")
print(the_dict)

# q2
import string
from operator import itemgetter


def open_file():
  # This is given. DO NOT CHANGE IT
  filename = input("Input a file name: \n")
  fpointer = open(filename)
  return fpointer


def main():
  fp = open_file()
  dict_of_words = {}
  lines = fp.readlines()
  fp.close()
  for line in lines:
    line = line.replace(",", " ")
    words = line.split()
    for word in words:
      word = word.strip().strip(string.punctuation)
      if not word:
        continue
      word = word.lower()
      if word not in dict_of_words:
        dict_of_words[word] = 0
      dict_of_words[word] += 1
  dict_of_words = sorted(dict_of_words.items(), key=itemgetter(0))
  print(dict_of_words)


main()

# q3
def add_to_dict(user_dict: dict, key, value):
  if key in user_dict:
    print("Error. Key already exists.")
  else:
    user_dict[key] = value


def remove_from_dict(user_dict: dict, key):
  if key not in user_dict:
    print("\nNo such key exists in the dictionary.")
  else:
    user_dict.pop(key)


def find_key(user_dict: dict, key):
  if key not in user_dict:
    print("\nKey not found.")
  else:
    print(f"\nValue: {user_dict[key]}")


def main():
  # DO NOT CHANGE THIS FUNCTION
  more = True
  D = {}
  while more:
    print("\n\nMenu: ")
    choice = input("\nadd(a), remove(r), find(f): ")
    if choice.lower() == "a":
      key = input("\nKey: ")
      value = input("\nValue: ")
      add_to_dict(D, key, value)
    elif choice.lower() == "r":
      key = input("\nKey to remove: ")
      remove_from_dict(D, key)
    elif choice.lower() == "f":
      key = input("\nKey to locate: ")
      find_key(D, key)
    else:
      print("\nInvalid choice.")

    do_more = input("\nMore (y/n)? ")
    if do_more.lower() != 'y':
      more = False
  if D:
    print()
    print(sorted(D.items()))


main()


