# q1
s = input("Input a string: \n")
first = s[0]
last = s[len(s) - 1]
print("{} {}".format(first, last))

# q2
s = input("Input a string: \n")
print(s[3:] + s[:3])

# q3
s = input("Input a string: \n")
for i in enumerate(range(len(s))):
  if s[i[0]] == "o":
    print(i[0])

# q4
s = input("Input a float: \n")
s_float = float(s)
print("{:>12.2f}".format(s_float))

# q5
s = input("Input a string: \n")
num = ""
for i in range(len(s)):
  if s[i].isdigit():
    num += s[i]
print(num)

# q6
name = input("Input a name: \n")
loc = name.find(",")
first_name = name[(loc + 2):]
last_name = name[:loc]
first_initial = first_name[:1].capitalize()
last_formatted = last_name[0:].capitalize() + last_name[:0]
final = "{}. {}".format(first_initial, last_formatted)
print(final)