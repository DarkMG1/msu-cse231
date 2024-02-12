"""
PROJECT HEADER GOES HERE
"""
import random

# DO NOT CHANGE THIS
random.seed(10)

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

INPUT = "\nWould you like to continue? (y/n) "


def fitness(target, individual):
    counter = 0
    for i in range(len(target)):
        if i >= len(individual):
            break
        if target[i] == individual[i]:
            counter += 1
    return counter / len(target)


def five_tournament_selection(population, target):
    best_individual = ""
    best_fitness = -1
    for _ in range(5):
        start_index = random.randint(0, NUM_POPULATION - 1) * len(target)
        end_index = start_index + len(target)
        prospect = population[start_index:end_index]
        prospect_fitness = fitness(target, prospect)
        if prospect_fitness > best_fitness:
            best_individual = prospect
            best_fitness = prospect_fitness
    return best_individual


def make_population(target):
    population = ""
    for i in range(NUM_POPULATION):
        for j in range(len(target)):
            population += random.choice(ALPHABET)
    return population


def mutation(individual):
    i = 0
    while i < len(individual):
        if random.random() < PROBABILITY_MUTATION:
            individual = individual[:i] + random.choice(ALPHABET) + individual[i + 1:]
        i += 1
    return individual


def single_point_crossover(individual1, individual2):
    mod_individual1, mod_individual2 = individual1, individual2
    if random.random() < PROBABILITY_CROSSOVER:
        random_crossover_point = random.randint(1, len(individual1))
        mod_individual1 = individual1[:random_crossover_point] + individual2[random_crossover_point:]
        mod_individual2 = individual2[:random_crossover_point] + individual1[random_crossover_point:]
    return mod_individual1, mod_individual2


def find_best_individual(population, target):
    best_individual = ""
    best_fitness = -1
    for _ in range(NUM_POPULATION):
        individual = five_tournament_selection(population, target)
        individual_fitness = fitness(target, individual)
        if individual_fitness > best_fitness:
            best_individual = individual
            best_fitness = individual_fitness
    return best_individual


def main():
    print(BANNER)
    enter = input(INPUT).lower()
    if enter != 'y':
        return
    while enter == 'y':
        stop = False
        target = input("\nPlease input the sentence you would like the program to guess: ").lower()
        invalid_input = True
        temp_target = target.replace(" ", "")
        while invalid_input:
            if temp_target.isalpha():
                invalid_input = False
            else:
                print("\nIncorrect input. Please try again.\n\n")
                target = input("Please input the sentence you would like the program to guess: ").lower()
                temp_target = target.replace(" ", "")
        print(target)
        population, best_individual = make_population(target), ""
        for i in range(NUM_GENERATIONS):
            if stop:
                break
            print("Generation: ", i)
            for j in range(NUM_POPULATION):
                individual1 = five_tournament_selection(population, target)
                individual2 = five_tournament_selection(population, target)
                individual1 = mutation(individual1)
                individual2 = mutation(individual2)
                individual1, individual2 = single_point_crossover(individual1, individual2)
                fitness_individual1 = fitness(target, individual1)
                fitness_individual2 = fitness(target, individual2)
                if fitness_individual1 == 1 or fitness_individual2 == 1:
                    print("I found the sentence early!")
                    if fitness_individual1 == 1:
                        best_individual = individual1
                    elif fitness_individual2 == 1:
                        best_individual = individual2
                    stop = True
                    break
                else:
                    if fitness_individual1 > fitness_individual2:
                        population = make_population(individual1)
                    else:
                        population = make_population(individual2)
        if not stop:
            best_individual = find_best_individual(population, target)
        print("Best Individual: ", best_individual)
        enter = input(INPUT).lower()
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
