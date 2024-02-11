##################################################
# Computer Project #3
#
# Inputs user for location, square footage, maximum monthly payment, down payment, and APR
# Outputs the cost of the house, the monthly payment, and the amortization schedule
#
# Sees if user can afford the house based on their maximum monthly payment
# Given a maximum monthly payment, finds the maximum square footage of a house the user can afford
#
##################################################

# All default values
NUMBER_OF_PAYMENTS = 360  # 30-year fixed rate mortgage, 30 years * 12 monthly payments
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668

# All language strings
WELCOME_TEXT = '''\nMORTGAGE PLANNING CALCULATOR\n============================ '''
MAIN_PROMPT = '''\nEnter a value for each of the following items or type 'NA' if unknown '''
LOCATIONS_TEXT = '''\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? '''
SQUARE_FOOTAGE_TEXT = '''\nWhat is the maximum square footage you are considering? '''
MAX_MONTHLY_PAYMENT_TEXT = '''\nWhat is the maximum monthly payment you can afford? '''
DOWN_PAYMENT_TEXT = '''\nHow much money can you put down as a down payment? '''
APR_TEXT = '''\nWhat is the current annual percentage rate? '''
AMORTIZATION_TEXT = '''\nWould you like to print the monthly payment schedule (Y or N)? '''
LOCATION_NOT_KNOWN_TEXT = '''\nUnknown location. Using national averages for price per square foot and tax rate.'''
NOT_ENOUGH_INFORMATION_TEXT = '''\nYou must either supply a desired square footage or a maximum monthly payment. 
Please try again.'''
KEEP_GOING_TEXT = '''\nWould you like to make another attempt (Y or N)? '''

# Loops until user does not want to continue
keep_going = "y"
while keep_going.lower() == "y":
    # Prints the welcome text and main prompt
    print(WELCOME_TEXT)
    print(MAIN_PROMPT)
    # Prompts user for location, square footage, maximum monthly payment, down payment, and APR
    location = input(LOCATIONS_TEXT)
    square_footage = input(SQUARE_FOOTAGE_TEXT)
    if square_footage.replace(".", "").isdigit():  # Checks if square footage is a float
        square_footage = float(square_footage)
    max_monthly_payment = input(MAX_MONTHLY_PAYMENT_TEXT)
    if max_monthly_payment.replace(".", "").isdigit():  # Checks if maximum monthly payment is a float
        max_monthly_payment = float(max_monthly_payment)
    down_payment = input(DOWN_PAYMENT_TEXT)
    if down_payment.replace(".", "").isdigit():  # Checks if down payment is a float
        down_payment = float(down_payment)
    else:
        down_payment = 0.0
    apr = input(APR_TEXT)
    if apr.replace(".", "").isdigit():  # Checks if APR is a float
        apr = float(apr) / 100
    else:
        apr = APR_2023
    property_tax_rate = 0.0
    price_per_sq_foot = 0.0
    # Sets property tax rate and price per square foot based on location
    if location == "Seattle":
        property_tax_rate = SEATTLE_PROPERTY_TAX_RATE
        price_per_sq_foot = SEATTLE_PRICE_PER_SQ_FOOT
    elif location == "San Francisco":
        property_tax_rate = SAN_FRANCISCO_PROPERTY_TAX_RATE
        price_per_sq_foot = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
    elif location == "Austin":
        property_tax_rate = AUSTIN_PROPERTY_TAX_RATE
        price_per_sq_foot = AUSTIN_PRICE_PER_SQ_FOOT
    elif location == "East Lansing":
        property_tax_rate = EAST_LANSING_PROPERTY_TAX_RATE
        price_per_sq_foot = EAST_LANSING_PRICE_PER_SQ_FOOT
    else:
        print(LOCATION_NOT_KNOWN_TEXT)
        property_tax_rate = AVERAGE_NATIONAL_PROPERTY_TAX_RATE
        price_per_sq_foot = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
        location = "the average U.S. housing market"

    # CASE 1 AND 2 - square footage is known and maximum monthly payment MAY be known (Line 103)
    if isinstance(square_footage, float):
        # Calculates home cost, principal, property taxes, monthly taxes, monthly payment with everything known
        home_cost = square_footage * price_per_sq_foot
        principal = home_cost - down_payment
        property_taxes = home_cost * property_tax_rate
        monthly_taxes = property_taxes / 12
        mpr = apr / 12
        monthly_payment = principal * (
                mpr * (1 + mpr)
                ** NUMBER_OF_PAYMENTS) / ((1 + mpr)
                                          ** NUMBER_OF_PAYMENTS - 1)
        # Prints out all information in an orderly fashion
        print('\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.'
              .format(location, square_footage, home_cost))
        print('A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:.1f}% APR results'
              .format(down_payment, apr * 100))
        print('\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'
              .format(monthly_taxes, monthly_payment, monthly_taxes + monthly_payment))

        # Sees if user can afford the house based on their maximum monthly payment.
        # If they did not provide a max monthly payment, this will not run.
        if isinstance(max_monthly_payment, float):
            if (monthly_payment + monthly_taxes) > max_monthly_payment:
                print("Based on your maximum monthly payment of ${:,.2f} you cannot afford this house."
                      .format(max_monthly_payment))
            else:
                print("Based on your maximum monthly payment of ${:,.2f} you can afford this house."
                      .format(max_monthly_payment))
        # Prints out the amortization schedule if the user wants it
        amortization = input(AMORTIZATION_TEXT)
        if amortization.lower() == "y":
            # Prints out header for amortization schedule
            print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format("Month", "Interest",
                                                        "Payment", "Balance"))
            print("================================================")
            printing = True
            month = 1
            remaining_balance = principal
            # Loops until 30 years or 360 months have passed
            while printing:
                if month > NUMBER_OF_PAYMENTS:
                    printing = False
                    break
                # Calculates interest payment, loan payment, and remaining balance
                interest_payment = remaining_balance * mpr
                loan_payment = monthly_payment - interest_payment
                print('{:^7d} | ${:>9,.2f} | ${:>10,.2f} | ${:>13,.2f}'
                      .format(month, interest_payment, loan_payment, remaining_balance))
                # Updates remaining balance and month
                remaining_balance -= loan_payment
                month += 1
    # CASE 3 - maximum monthly payment is known
    elif isinstance(max_monthly_payment, float) and isinstance(square_footage, str):
        # Finds the maximum square footage of a house the user can afford
        square_footage = 100
        home_cost, principal, property_taxes, monthly_taxes, mpr, \
            monthly_payment = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        # Loops until the monthly payment is greater than the maximum monthly payment
        matched = False
        while True:
            home_cost = square_footage * price_per_sq_foot
            principal = home_cost - down_payment
            property_taxes = home_cost * property_tax_rate
            monthly_taxes = property_taxes / 12
            mpr = apr / 12
            monthly_payment = principal * (
                    mpr * (1 + mpr)
                    ** NUMBER_OF_PAYMENTS) / ((1 + mpr)
                                              ** NUMBER_OF_PAYMENTS - 1)
            # If the monthly payment is greater than the maximum monthly payment, the square footage is decreased
            # by 1. The loop is run one more time to recalculate everything with the decreased square footage
            # and then it breaks.
            if matched:
                break
            elif (monthly_payment + monthly_taxes) > max_monthly_payment:
                square_footage -= 1
                matched = True
            else:
                # If the monthly payment is less than the maximum monthly payment, the square footage is increased
                square_footage += 1
        # Prints out all information in an orderly fashion
        print("\n\nIn {}, a maximum monthly payment of ${:,.2f} allows the purchase of a house of {:,.0f} sq. feet "
              "for ${:,.0f}"
              .format(location, max_monthly_payment, square_footage, home_cost))
        print("\tassuming a 30-year fixed rate mortgage with a ${:,.0f} down payment at {:.1f}% APR."
              .format(down_payment, apr * 100))
    # CASE 4 - not enough information
    else:
        # Prints out error message if not enough information is given
        print(NOT_ENOUGH_INFORMATION_TEXT)
        continue
    # Prompts user if they want to continue
    keep_going = input(KEEP_GOING_TEXT)
