##################################################
# Computer Project #6
#
# Inputs: 3 files: a names file, a Twitter id file and a facebook id file
#        A menu choice
# Processing: Reads the files and processes the data
#             according to the menu choice
# Outputs: The result of the menu choice
#
##################################################
import sys
from typing import TextIO

# def input( prompt=None ):
#     """
#         DO NOT MODIFY: Uncomment this function when submitting to Codio
#         or when using the run_file.py to test your code.
#         This function is needed for testing in Codio to echo the input to the output
#         Function to get user input from the standard input (stdin) with an optional prompt.
#         Args:
#             prompt (str, optional): A prompt to display before waiting for input. Defaults to None.
#         Returns:
#             str: The user input received from stdin.
#     """
#
#     if prompt:
#         print( prompt, end="" )
#     aaa_str = sys.stdin.readline()
#     aaa_str = aaa_str.rstrip( "\n" )
#     print( aaa_str )
#     return aaa_str


choices = '''
  Menu : 
     1: Max number of friends intersection between X and Facebook among all
     2: Percentage of people with no shared friends between X and Facebook
     3: Individual information
     4: Percentage of people with  more friends in X compared to Facebook
     5: The number of  triangle friendships in X
     6: The number of  triangle friendships on Facebook
     7: The number of  triangle friendships in X and Facebook together 
       Enter any other key(s) to exit

  '''

def open_file(prompt: str) -> TextIO:
    """Open a file with the given prompt. If the file does not exist, prompt the user again."""
    while True:
        try:
            filename = input(prompt)
            in_file = open(filename, "r")
            break
        except IOError:
            print("Error. File does not exist")
    return in_file

def format_data(data: list) -> list:
    """Format the data from the file into a list of sets."""
    result = []
    for line in data:
        # Remove empty strings from the list
        if line.strip():
            # Split the line into a list of items and remove empty strings
            items = line.strip().split(',')
            non_empty_items = set(item for item in items if item)
            result.append(non_empty_items)
        else:
            # Add an empty set if the line is empty
            result.append(set())
    return result

def build_structures(names_file: TextIO, twitter_file: TextIO, facebook_file: TextIO) -> dict:
    """Build the data structures for the names, Twitter and Facebook data."""

    # Read the names, Twitter and Facebook data and creates sets of friends for each person
    names = [name.strip() for name in names_file.readlines()]
    twitter_ids = format_data(twitter_file.readlines())
    facebook_data = format_data(facebook_file.readlines())

    twitter_data = []

    # Converts the Twitter ids to names
    for lists in twitter_ids:
        name_set = set()
        for user_id in lists:
            name = names[int(user_id)]
            name_set.add(name)
        twitter_data.append(name_set)

    # Creates a dictionary with the names as keys and the Twitter and Facebook data as values
    data = {}
    for i in range(len(names)):
        data[names[i]] = {
            'Twitter': twitter_data[i],
            'Facebook': facebook_data[i]
        }

    # Close the files
    names_file.close()
    twitter_file.close()
    facebook_file.close()
    return data

def max_intersection(data: dict) -> int:
    """Find the maximum number of friends intersection between X and Facebook among all."""
    max_intersection = 0
    for name in data:
        # Find the intersection of friends between X and Facebook
        twitter_friends = data[name]['Twitter']
        facebook_friends = data[name]['Facebook']
        intersection = twitter_friends.intersection(facebook_friends)
        if len(intersection) > max_intersection:
            # Update the maximum intersection if the current intersection is greater
            max_intersection = len(intersection)
    return max_intersection

def unique_friends(data: dict) -> float:
    """Find the percentage of people with no shared friends between X and Facebook."""
    unique = 0
    for name in data:
        # Check if the intersection of friends between X and Facebook is empty
        if len(data[name]['Twitter'].intersection(data[name]['Facebook'])) == 0:
            unique += 1

    # Calculate the percentage of people with no shared friends
    return round((unique/len(data))*100)

def individual_info(data: dict, name: str) -> dict:
    """Return the individual information for the given name."""
    information = {}
    if name in data:
        # Sort the friends and store them in a dictionary
        twitter_friends : set = data[name]['Twitter']
        facebook_friends : set = data[name]['Facebook']
        sorted_twitter_friends = sorted(twitter_friends)
        sorted_facebook_friends = sorted(facebook_friends)
        information = {"Twitter": sorted_twitter_friends, "Facebook": sorted_facebook_friends}
    return information


def more_friends(data: dict) -> float:
    """Find the percentage of people with more friends in X compared to Facebook."""
    counter = 0
    for name in data:
        # Check if the number of friends in X is greater than the number of friends in Facebook
        if len(data[name]['Twitter']) > len(data[name]['Facebook']):
            counter += 1
    # DIvide the number of people with more friends in X by the total number of people
    return round((counter/len(data))*100)
    pass

def create_friendship_sets(data: dict, network: str) -> dict:
    """Prepare friendship sets for the specified network ('Twitter', 'Facebook', or 'Combined')."""
    friendship_sets = {}
    for person, networks in data.items():
        if network == 'Combined':
            # Merge Twitter and Facebook friends for the 'Combined' network
            friends = networks['Twitter'].union(networks['Facebook'])
        else:
            friends = networks[network]
        friendship_sets[person] = friends
    return friendship_sets

def count_triangle_friendships(friendship_sets: dict) -> int:
    """Count the triangle friendships in the given friendship sets."""
    counted_triangles = set()
    for person, friends in friendship_sets.items():
        for friend1 in friends:
            for friend2 in friends - {friend1}:
                # Ensure friend1 and friend2 are also friends and avoid double-counting triangles
                if friend1 in friendship_sets and friend2 in friendship_sets[friend1] and \
                   (tuple(sorted([person, friend1, friend2])) not in counted_triangles):
                    counted_triangles.add(tuple(sorted([person, friend1, friend2])))
    return len(counted_triangles)


def main():
    # Open the files
    names_file = open_file("\nEnter a names file ~:")
    twitter_file = open_file("\nEnter the twitter id file ~:")
    facebook_file = open_file("\nEnter the facebook id file ~:")

    # Build the data structures
    data = build_structures(names_file, twitter_file, facebook_file)

    # Display the menu and continue to prompt the user for a choice
    while True:
        print(choices)
        choice = input("Input a choice ~:")
        # Process the choice
        match choice:
            case "1":
                # Find the maximum number of friends intersection between X and Facebook among all
                # and display the result
                print("The Max number intersection of friends between X and Facebook is: {}".format(
                    max_intersection(data)))
            case "2":
                # Find the percentage of people with no shared friends between X and Facebook
                # and display the result
                print("{}% of people have no friends in common on X and Facebook".format(
                    unique_friends(data)))
            case "3":
                # Display the individual information for the given name
                # Continue to prompt the user for a name if the name is invalid
                while True:
                    name = input("Enter a person's name ~:")
                    info = individual_info(data, name)
                    # If info is empty, the name is invalid
                    if not info:
                        print("Invalid name or does not exist")
                        continue
                    # Print out information
                    print("-"*14+"\nFriends in X\n"+"*"*14)
                    for name in info['Twitter']:
                        print(name)
                    print("-"*20+"\nFriends in Facebook\n"+"*"*20)
                    for name in info['Facebook']:
                        print(name)
                    break
            case "4":
                # Find the percentage of people with more friends in X compared to Facebook
                # and display the result
                print("{}% of people have more friends in X compared to Facebook".format(
                    more_friends(data)))
            case "5":
                # Prepare friendship sets for the Twitter network
                twitter_friendships = create_friendship_sets(data, 'Twitter')
                # Count the triangle friendships in the Twitter network and display the result
                x_triangles = count_triangle_friendships(twitter_friendships)
                print("The number of triangle friendships in X is: {}".format(x_triangles))
            case "6":
                # Prepare friendship sets for the Facebook network
                facebook_friendships = create_friendship_sets(data, 'Facebook')
                # Count the triangle friendships in the Facebook network and display the result
                fb_triangles = count_triangle_friendships(facebook_friendships)
                print("The number of triangle friendships in Facebook is: {}".format(fb_triangles))
            case "7":
                # Prepare friendship sets for the combined network
                combined_friendships = create_friendship_sets(data, 'Combined')
                # Count the triangle friendships in the combined network and display the result
                combined_triangles = count_triangle_friendships(combined_friendships)
                print("The number of triangle friendships in X merged with Facebook is: {}".format(combined_triangles))
            case _:
                print("Thank you")
                exit(0)



if __name__ == '__main__':
    main()