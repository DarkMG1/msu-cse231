# q1
num_str = input("Input an int: \n")
num_int = int(num_str)
n = 1
while n <num_int:
  print(n)
  n+=1

# q2
num_str = input("Input an int: \n")
total = 0
while num_str != '10':
  num_int = int(num_str)
  total+=num_int
  num_str = input("Input an int: \n")
print(total)

# q3
n_str = input("Input an int: \n")
n_int = int(n_str)
n = 0
while n <= (n_int - 1):
    print(1 + (2 * n))
    n += 1

# q4
n_str = input("Input an int: \n")
n_int = int(n_str)
count = 1;
while count <= n_int:
  if n_int % count == 0:
    print(count)
  count+=1

# q5
m = input("Input the first integer: \n")
n = input("Input the second integer: \n")
m_int = int(m)
n_int = int(n)
while n_int:
  m_int,n_int = n_int, m_int % n_int
print(m_int)
