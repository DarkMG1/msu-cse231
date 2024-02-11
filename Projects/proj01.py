##################################################
# Computer Project #1
#
# Input: 1 (number of rods)
# Output: Conversions to meters, feet, miles
#         furlongs and minutes to walk the rods
#         given
# Rounds conversion to 3 decimal places.
#
##################################################

# Takes input of rods from user
rods_str = input("Input rods: ")
rods_float = float(rods_str)  # Converts to float

print("\nYour value is", rods_float, "rods.\n")

# Converts rods to given conversion factors
meters = rods_float * 5.0292
furlongs = rods_float / 40
miles = meters / 1609.34
feet = meters / 0.3048
minutes = (miles / 3.1) * 60

# Prints out conversions in a readable format
print("Conversions")
print("Meters:", round(meters, 3))
print("Feet:", round(feet, 3))
print("Miles:", round(miles, 3))
print("Furlongs:", round(furlongs, 3))
print("Minutes to walk", rods_float, "rods:", round(minutes, 3))
