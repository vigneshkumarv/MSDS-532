"""
Assignment 4 Problem 1: find and count matching strings
September 27, 2023
Vignesh Kumar Venkateshwar
"""

from string import *

def countSubstrMatches(srch_str, sub_str):
    """
    Purpose: Count the number of times a substring matches with the input string iteratively
    Arguments: srch_str (string searched) and sub_str (sub-string to search)
    Return: Match count
    """
    count = -1                                      # Initialize count to -1 (initial)
    if len(srch_str) == 0 or len(sub_str) == 0:     # Check if both the strings are input by the user
        return count
    count = index = 0
    sub_str_len = len(sub_str)                      # Determine the length of sub-string
    while index < len(srch_str):                    # Loop until index is less than length of search string
        pos = srch_str.find(sub_str, index)         # Find the position of sub-string in the search string
        if(pos != -1):
            count +=1                               # Increment count by one
            if sub_str_len != 1:
                index = pos + sub_str_len - 1
            else:
                index = pos + sub_str_len
        else:
            break                                   # Break out of while loop if sub-string is not found
    return count


def recursive_count(srch_str, sub_str, index):
    """
    Purpose: recursive function which counts the number of sub-string matches
    Arguments: srch_str (string searched), sub_str (sub-string to search) and index
    Return: Sub-string match count
    """
    sub_str_len = len(sub_str)                      # Determine the length of sub-string
    index = srch_str.find(sub_str, index)           # Find the position of sub-string in the search string
    if index == -1:
        return 0                                    # Return zero if sub-string is not found
    else:
        if sub_str_len != 1:
            return 1 + recursive_count(srch_str, sub_str, index+sub_str_len-1)
        else:
            return 1 + recursive_count(srch_str, sub_str, index+sub_str_len)


def countSubstrRecursive(srch_str, sub_str):
    """
    Purpose: Count the number of times a substring matches with the input string recursively
    Arguments: srch_str (string searched) and sub_str (sub-string to search)
    Return: Match count or -1
    """
    if len(srch_str) == 0 or len(sub_str) == 0:     # Check if both the strings are input by the user
        return -1                                   # Return -1 if one or both of input strings are missing
    else:
        return recursive_count(srch_str, sub_str, 0)


# Main program for debugging
"""
search_string = input("Enter search string: ")
sub_string = input("Enter sub-string to be searched: ")
matches = countSubstrRecursive(search_string, sub_string)
if matches != -1:
    print("No. of matches of '{0}' in '{1}' is {2}.".format(sub_string, search_string, matches))
else:
    print("one or both of the input strings are missing!")
"""