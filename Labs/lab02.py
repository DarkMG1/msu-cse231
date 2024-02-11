##############################################################################
#
# LAB 2
#
# Allows user to input integers until 0 is entered.
# Prints the sum of the odd integers, the sum of the even integers,
# the count of the odd integers, the count of the even integers,
# and the total count of positive integers entered.
##############################################################################
n_str = input("\nInput an integer (0 terminates): ")

even_sum, even_count, odd_sum, odd_count, positive_int_count = 0, 0, 0, 0, 0

# While loop to allow inputs until 0 is entered
while n_str != '0':
    n_int = int(n_str)
    if n_int < 0:  # Ignore negative integers
        n_str = input("Input an integer (0 terminates): ")
        continue
    else:
        positive_int_count += 1
    if n_int % 2 == 0:  # Check if even or odd
        even_sum += n_int
        even_count += 1
    else:
        odd_sum += n_int
        odd_count += 1
    n_str = input("Input an integer (0 terminates): ")

# Do not change the following lines of code
print("\n")
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)