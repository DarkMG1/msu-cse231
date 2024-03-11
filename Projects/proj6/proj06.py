""" Source header """

import sys

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

"Input a choice ~:"

"Error. File does not exist"
"\nEnter a names file ~:"
"\nEnter the X id file ~:"
"\nEnter the facebook id file ~:"

"The Max number intersection of friends between X and Facebook is: {}"
"{}% of people have no friends in common on X and Facebook"

"Enter a person's name ~:"
print("-"*14+"\nFriends in X\n"+"*"*14)
print("-"*20+"\nFriends in Facebook\n"+"*"*20)
"Invalid name or does not exist"

"{}% of people have more friends in X compared to Facebook"

"The number of triangle friendships in X is: {}"
"The number of triangle friendships in Facebook is: {}"
"The number of triangle friendships in X merged with Facebook is:  {}"
"Thank you"


def open_file():
    pass




def main():
    pass


if __name__ == '__main__':
    main()