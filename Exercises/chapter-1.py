# q1
m_str = input('Input m: \n')  # do not change this line
# change m_str to a float
# remember you need c
# e =
c = 300000000
m_float = float(m_str)
e = (m_float * (pow(c, 2)))
print("e =", e)  # do not change this line

# q2
in_str = input("Input s: \n")
in_int = int(in_str)
print("in_int = ", in_int)
in_float = float(in_int)
print("in_float = ", in_float)

# q3
x1_str = input("\nInput x1: ") # do not change this line
y1_str = input("\nInput y1: ") # do not change this line
x2_str = input("\nInput x2: ") # do not change this line
y2_str = input("\nInput y2: ") # do not change this line

x1_int = int(x1_str)
y1_int = int(y1_str)
x2_int = int(x2_str)
y2_int = int(y2_str)
d_sq = (pow(x2_int - x1_int,2)+pow(y2_int - y1_int, 2))
d = pow(d_sq,1/2)
print("\nd =",d)

# q4
secs_str = input("Input seconds: ")
secs_int = int(secs_str)
rem = secs_int % 3600
hours = (secs_int - rem) / 3600
seconds = rem % 60
minutes = (rem - seconds) / 60
hours = int(hours)
minutes = int(minutes)
print("\n",hours,":",minutes,":",seconds)