###########################################################
#  Computer Project #8
#
#    prompt for an action corresponding with a force
#    input a valid force
#    depending on the action: add, remove, show, find, compute, reset, or stop
#    for add, remove, find, and compute: input the name of the force
#    for add: input the magnitude and angle of the force
#    for find: print the force components
#    for compute: print the resultant force
#    for show: print all the forces
#    for reset: reset the calculator
#    for stop: stop the program
#    print the result of the action
#    if the action is invalid, print an error message
#    repeat until the user stops the program
###########################################################

from proj8_force import ForceCalculator
import sys

MENU = '''\n:~Net Force Calculator Program
          1) Add force
          2) Remove force
          3) Show forces
          4) Find force components
          5) Compute resultant force
          6) Reset calculator
          7) Stop the program
          Enter option~:'''

def prompt_num(prompt_str: str) -> float:
    """
    Prompts the user for a float
    :param prompt_str: Prompt to show user
    :return: float: user input
    """
    while True:
        user = input(prompt_str)
        try:
            return float(user)
        except ValueError:
            print("\nInput {} is not a valid float number!".format(user))
            continue


def main():
    # Create a ForceCalculator object
    force_calculator = ForceCalculator()

    # Loops until the user chooses to stop the program
    while True:

        # Prompts the user for an action
        option = input(MENU).strip()
        match option:
            case "1":
                # Adds a force to the calculator
                name = input("\n:~Enter name of force~:").strip()
                magnitude = prompt_num("\n:~Enter value for {}~:"
                                       .format("Magnitude (N)"))
                angle = prompt_num("\n:~Enter value for {}~:"
                                   .format("Angle (degrees)"))
                try:
                    force_calculator.add_force(name, magnitude, angle)
                except RuntimeError as e:
                    print(e)
            case "2":
                # Removes a force from the calculator
                name = input("\n:~Enter name of force~:").strip()
                try:
                    force_calculator.remove_force(name)
                except RuntimeError as e:
                    print(e)
            case "3":
                # Shows all forces in the calculator
                if not force_calculator.get_forces():
                    print("\nThere are no force objects in the calculator.")
                else:
                    print("\nForce objects in the calculator")
                    print(force_calculator)
            case "4":
                # Finds the force components of a force in the calculator
                name = input("\n:~Enter name of force~:").strip()
                try:
                    force = force_calculator[name]
                except RuntimeError as e:
                    print(e)
                    continue
                print("\nForce components for Force object {}:".format(name))
                print(force)
            case "5":
                # Computes the resultant force of all forces in the calculator
                print("\nResultant force of all forces in the calculator")
                print(force_calculator.compute_net_force())
            case "6":
                # Resets the calculator
                force_calculator = ForceCalculator()
            case "7":
                # Stops the program
                break
            case _:
                # Invalid option
                print("\nInvalid option. Please Try Again!")
                continue


if __name__ == "__main__":
    main()
