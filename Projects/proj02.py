##############################################################################
#
# PROJECT 2
#
# Prompts user for a galactic code, number of days, odometer at liftoff,
# and odometer at touchdown. Calculates the cost of the rental and prints
# a summary.
#
##############################################################################

# Imports the math module
import math

# All language strings
INTERGALACTIC_BANNER = """
Welcome to SpaceX Galactic Car Extravaganza!

Prepare for an interstellar joyride with our cosmic cruisers!
At the prompt, please enter:
- Galactic code (XV, ET, SI)
- Days of your interstellar joyride
- Odometer at liftoff
- Odometer at touchdown
"""
INTERGALACTIC_PROMPT = "Ready for an out-of-this-world adventure (Y/X)? "
INVALID_CODE_PROMPT = "\n*** Invalid galactic code. Retry! ***"
CUSTOMER_CODE_INPUT = "\nGalactic code (XV, ET, SI): "
RENTAL_DAYS_INPUT = "\nNumber of days (int): "
START_ODOMETER_INPUT = "\nOdometer at liftoff (int): "
END_ODOMETER_INPUT = "\nOdometer at touchdown (int):   "

# Prints the banner and prompts the user to begin
print(INTERGALACTIC_BANNER)
ready = input(INTERGALACTIC_PROMPT)
if ready != 'Y':  # Exits if user does not enter 'Y'
    print("\nThank you for entrusting us with your joyride!")
    exit(0)
while ready == 'Y':  # Loops until user enters 'X'
    galactic_code = input(CUSTOMER_CODE_INPUT)
    while not (galactic_code == 'XV' or galactic_code == 'ET'
               or galactic_code == 'SI'): # Loops until valid code is entered
        print(INVALID_CODE_PROMPT)
        galactic_code = input(CUSTOMER_CODE_INPUT)
    # Prompts user for rental days and odometer readings
    rental_days = float(input(RENTAL_DAYS_INPUT))
    start_odometer = float(input(START_ODOMETER_INPUT))
    end_odometer = float(input(END_ODOMETER_INPUT))
    light_years = 0
    # Calculates light years traveled
    if start_odometer > end_odometer:
        light_years = 1000000 - start_odometer
        light_years += end_odometer
        light_years = light_years / 10
    else:
        light_years = ((end_odometer - start_odometer) / 10)
    cost = 0
    # Calculates cost of rental based on galactic code
    if galactic_code == 'XV':
        cost = rental_days * 40.00
        cost += light_years * 0.25
    elif galactic_code == 'ET':
        cost = rental_days * 60.00
        # Calculates average light years per day
        avg_light_years = light_years / rental_days
        if avg_light_years >= 100:
            # Adds extra cost if average light years per day is greater than 100
            cost += (avg_light_years - 100) * rental_days * 0.25
    elif galactic_code == 'SI':
        # Calculates rental weeks
        rental_weeks = math.ceil(rental_days / 7)
        cost = rental_weeks * 190.00
        avg_light_years = light_years / rental_weeks
        if avg_light_years >= 1500:
            # Adds extra cost if average light years per week is greater than 1500
            cost += (light_years - (1500 * rental_weeks)) * 0.25
            cost += rental_weeks * 200.00
        elif avg_light_years >= 900:
            # Adds extra cost if average light years per week is greater than 900
            cost += rental_weeks * 100.00

    # Prints summary of rental
    print("\nGalactic traveler summary:")
    print("\tCode:", galactic_code)
    print("\tDays in orbit:", int(rental_days))
    print("\tLiftoff odometer:", int(start_odometer))
    print("\tTouchdown odometer:", int(end_odometer))
    print("\tLight-years traveled:", light_years)
    print("\tCost in star credits: $", round(cost, 2))
    # Prompts user to continue or exit
    ready = input(INTERGALACTIC_PROMPT)
print("\nThank you for entrusting us with your joyride!")
