# q1
def new_list_function(initial_list):
  new_list = []
  for i in range(3):
    for each in initial_list:
      new_list.append(each)
  return new_list

def main():
  initial_list = []
  while True:
    input_str = input('Enter value to be added to list: \n')
    if input_str.lower() == "exit":
      break
    initial_list.append(input_str)
  new_list = new_list_function(initial_list)
  for line in new_list:
    print(line)

main()

# q2
def return_list(user_str):
  user_str = user_str.replace(",", " ")
  if user_str.find(' ') == -1:
    return user_str
  words = user_str.split(" ")
  return words

def main():
  the_string = input("Enter the string: \n")
  result = return_list(the_string)
  print(result)

main()

# q3
def mutate_list(user_list, index, value):
  return user_list.insert(index, value)

def reverse_list(user_list):
  user_list.reverse()
  return user_list

def remove_index(user_list, index):
  print("Total elements in list = ", len(user_list))
  user_list.pop(index)
  print("Total elements in list = ", len(user_list))
  return user_list

def main():
  user_list = input("Enter values in list separated by commas: \n")
  user_list = user_list.split(",")
  user_list = [int(i) for i in user_list]
  print(user_list)
  print("Menu: ")
  print("mutate list(m), remove (r), reverse_list (R)")
  user_choice = input("Enter choice (m,r,R): \n")
  if user_choice == 'm':
    index_num, v = input("\n").split(",")
    index_num = int(index_num)
    v = int(v)
    mutate_list(user_list, index_num, v)
    print(user_list)
  elif user_choice == 'r':
    index_num = int(input("\n"))
    remove_index(user_list, index_num)
    print(user_list)
  elif user_choice == 'R':
    new_list = reverse_list(user_list)
    print(new_list)

main()

# q4
def list_to_tuple(user_list):
  result_list = []
  try:
    for each in user_list:
      result_list.append(int(each))
  except ValueError:
    print("Error. Please enter only integers.")
    exit(0)
  print(tuple(result_list))

def main():
  a_list = input("Enter elements of list separated by commas: \n").strip().split(',')
  list_to_tuple(a_list)

main()
