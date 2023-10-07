"""
Assignment 4 Problem 2: find matching indices of sub-string in the search-string
September 27, 2023
Vignesh Kumar Venkateshwar
"""

from string import *

def allMatchesIndices(srch_str, sub_str):
    """
    Purpose: Find all matching indices of sub-string in the search string
    Arguments: srch_str (string searched) and sub_str (sub-string to search)
    Return: tuple of matching indices or -1
    """
    if len(srch_str) == 0 or len(sub_str) == 0:         # Check if both the strings are input by the user
        return -1
    matched_indices = []                                # Initialize matched_indices to an empty list
    index = 0                                           # Initialize index to zero
    sub_str_len = len(sub_str)                          # Determine the length of sub-string
    while index < len(srch_str):                        # Loop until index is less than length of search string
        pos = srch_str.find(sub_str, index)             # Find the position of sub-string in the search string
        if pos != -1:
            matched_indices.append(pos)                 # Append pos (position) into the list
            if sub_str_len != 1:
                index = pos + sub_str_len -1
            else:
                index = pos + sub_str_len
        else:
            break                                       # Break out of while loop if sub-string is not found
    return tuple(matched_indices)                       # Return matched_indices as a tuple


# Main program for debugging
""""
search_string = input("Enter search string: ")
sub_string = input("Enter sub-string to be searched: ")
matching_indices = allMatchesIndices(search_string, sub_string)
if matching_indices != -1:
    print(matching_indices)
else:
    print("one or both of the input strings are missing!")
"""