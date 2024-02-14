##################################################
# Computer Project #4
#
# Inputs a sentence and attempts to guess it using a genetic algorithm
# Outputs the best individual from the population
#
# Uses a genetic algorithm to guess the sentence
#
##################################################
import random

# DO NOT CHANGE THIS
random.seed(10)

# Constants
NUM_GENERATIONS = 200
NUM_POPULATION = 100
PROBABILITY_MUTATION = 0.2
PROBABILITY_CROSSOVER = 0.8
ALPHABET = 'abcdefghijklmnopqrstuvwxyz '

BANNER = """
**************************************************************
Welcome to GeneticGuess Sentencer! 
This program will attempt to guess a sentence that you input. 
Simply input a sentence and the program will attempt to guess it!
**************************************************************
"""

# INPUT STRING
INPUT = "\nWould you like to continue? (y/n) "


# FITNESS FUNCTION
def fitness(target, individual):
    counter = 0
    # Compares the individual to the target
    for i in range(len(target)):
        # If the individual is longer than the target, break
        if i >= len(individual):
            break
        # For each character individual and target are the same, add 1 to the counter
        if target[i] == individual[i]:
            counter += 1
    # Returns the counter divided by the length of the target
    return counter / len(target)

# FIVE TOURNAMENT SELECTION FUNCTION
def five_tournament_selection(population, target):
    # Initializes the best individual and best fitness
    best_individual = ""
    best_fitness = -1
    for _ in range(5):
        # Randomly selects a starting index from the population
        start_index = random.randint(0, NUM_POPULATION - 1) * len(target)
        # Sets the ending index to the starting index plus the length of the target
        end_index = start_index + len(target)
        # Sets the prospect to the individual at the starting and ending index
        prospect = population[start_index:end_index]
        # Calculates the fitness of the prospect
        prospect_fitness = fitness(target, prospect)
        # If the fitness of the prospect is greater than the best fitness,
        # set the best individual and best fitness to the prospect and its fitness
        if prospect_fitness > best_fitness:
            best_individual = prospect
            best_fitness = prospect_fitness
    # Returns the best individual
    return best_individual

# MAKE POPULATION FUNCTION
def make_population(target):
    # Initializes the population
    population = ""
    # Depending on the NUM_POPULATION constant, for each character in the target, add a random character from the
    # alphabet to the population
    for i in range(NUM_POPULATION):
        for j in range(len(target)):
            population += random.choice(ALPHABET)
    return population

# MUTATION FUNCTION
def mutation(individual):
    i = 0
    # For each character in the individual, if a random number is less than or equal to the PROBABILITY_MUTATION
    # constant, replace the character at the index with a random character from the alphabet
    while i < len(individual):
        if random.random() <= PROBABILITY_MUTATION:
            individual = individual[:i] + random.choice(ALPHABET) + individual[i + 1:]
        i += 1
    # Returns the individual
    return individual

# SINGLE POINT CROSSOVER FUNCTION
def single_point_crossover(individual1, individual2):
    # Initializes the mod_individuals to the individuals
    mod_individual1, mod_individual2 = individual1, individual2
    # If a random number is less than or equal to the PROBABILITY_CROSSOVER constant, set a random crossover point
    if random.random() <= PROBABILITY_CROSSOVER:
        # Set the random crossover point to a random number between 1 and the length of the individual
        random_crossover_point = random.randint(1, len(individual1))
        # Set the mod_individuals to the individuals with the crossover point
        mod_individual1 = individual1[:random_crossover_point] + individual2[random_crossover_point:]
        mod_individual2 = individual2[:random_crossover_point] + individual1[random_crossover_point:]
    # Returns the mod_individuals
    return mod_individual1, mod_individual2

# FIND BEST INDIVIDUAL FUNCTION
def find_best_individual(population, target):
    # Initializes the best individual, the best fitness, start index, and end index
    best_individual = ""
    best_fitness = -1
    start_index = 0
    end_index = len(target)
    # For each individual in the population, set the prospect to the individual at the start and end index
    # Calculate the fitness of the prospect and if the fitness is greater than the best fitness, set the best individual
    # and best fitness to the prospect and its fitness
    for _ in range(NUM_POPULATION):
        prospect = population[start_index:end_index]
        prospect_fitness = fitness(target, prospect)
        if prospect_fitness > best_fitness:
            best_individual = prospect
            best_fitness = prospect_fitness
        # Increment the start and end index by the length of the target
        start_index += len(target)
        end_index += len(target)
    # Returns the best individual
    return best_individual

# MAIN FUNCTION
def main():
    # Prints the banner and asks the user if they would like to continue
    print(BANNER)
    enter = input(INPUT).lower()
    if enter != 'y':
        return
    # While the user would like to continue, the program will run
    while enter == 'y':
        stop = False
        # Asks the user for the sentence they would like the program to guess
        target = input("\nPlease input the sentence you would like the program to guess: ").lower()
        invalid_input = True
        # Checks if the input is valid
        temp_target = target.replace(" ", "")
        while invalid_input:
            if temp_target.isalpha():
                invalid_input = False
            else:
                # If the input is invalid, ask the user to input the sentence again
                print("\nIncorrect input. Please try again.\n\n")
                target = input("Please input the sentence you would like the program to guess: ").lower()
                temp_target = target.replace(" ", "")
        # Initializes the population and best individual
        population, best_individual = make_population(target), ""
        print("\nGeneticGuess results:")
        # For each generation, the program will run the genetic algorithm
        for i in range(NUM_GENERATIONS):
            # If the target sentence is found, break
            if stop:
                break
            print("Generation: ", i)
            new_population = ""
            # For each individual in the population, run the genetic algorithm
            for j in range(NUM_POPULATION):
                # Selects two individuals from the population and mutates them
                individual1 = five_tournament_selection(population, target)
                individual2 = five_tournament_selection(population, target)
                individual1 = mutation(individual1)
                individual2 = mutation(individual2)
                # Performs single point crossover on the two individuals
                individual1, individual2 = single_point_crossover(individual1, individual2)
                # Calculates the fitness of the two individuals and if one of the individuals is the target, break
                fitness_individual1 = fitness(target, individual1)
                fitness_individual2 = fitness(target, individual2)
                if fitness_individual1 == 1:
                    best_individual = individual1
                    new_population += individual1
                    stop = True
                elif fitness_individual2 == 1:
                    best_individual = individual2
                    new_population += individual2
                    stop = True
                # If the fitness of the first individual is greater than the second, add the first individual to the new
                # population. If the fitness of the second individual is greater than or equal to the first, add the
                # second individual to the new population.
                elif fitness_individual1 > fitness_individual2:
                    new_population += individual1
                elif fitness_individual2 >= fitness_individual1:
                    new_population += individual2
            # Sets the old population to the new population
            population = new_population
        # If the target sentence is found, print the sentence early. If not, find the best individual and print it
        # out to the user
        if stop:
            print("\nI found the sentence early!")
        else:
            best_individual = find_best_individual(population, target)
        print("Best Individual: ", best_individual)
        # Asks the user if they would like to continue
        enter = input(INPUT).lower()
        # If the user does not want to continue, print a thank-you message and return
        if enter != 'y':
            print("\nThank you for using GeneticGuess Sentencer!")
            return


# These two lines allow this program to be imported into other codes
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
# DO NOT CHANGE THESE 2 lines or Do NOT add code to them. Everything
# you add should be in the 'main' function above.
if __name__ == '__main__':
    main()
