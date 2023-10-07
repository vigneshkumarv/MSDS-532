"""
Assignment 4 Problem 4: find fuzzy matches which are not an exact match
October 1, 2023
Vignesh Kumar Venkateshwar
"""

import random
from string import *

def allMatchedIndices(srch_str, sub_str):
    """
    Purpose: Find all matching indices of sub-string in the search string
    Arguments: srch_str (string searched) and sub_str (sub-string to search)
    Return: tuple of matching indices or -1
    """
    matched_indices = []                                                        # Initialize matched_indices to an empty list
    index = 0                                                                   # Initialize index to zero
    sub_str_len = len(sub_str)                                                  # Determine the length of sub-string
    while index < len(srch_str):                                                # Loop until index is less than length of search string
        pos = srch_str.find(sub_str, index)                                     # Find the position of sub-string in the search string
        if pos != -1:
            matched_indices.append(pos)                                         # Append pos (position) into the list
            if sub_str_len != 1:
                index = pos + sub_str_len -1
            else:
                index = pos + sub_str_len
        else:
            break                                                               # Break out of while loop if sub-string is not found
    return tuple(matched_indices)                                               # Return matched_indices as a tuple


def random_split(input_str):
    """
    Purpose: Split input string based on a random character
    Argument: input_str (string)
    Return: two strings or none
    """
    if len(input_str) <= 1:
        return None, None
    
    sep_char = random.choice(input_str)
    parts = input_str.split(sep_char, 1)
    if len(parts) == 1:
        return None, None
    
    return parts[0], parts[1]


def fuzzyMatching(subOne, subTwo, len_sub_str_One):
    """
    Purpose: Find fuzzy matches
    Arguments: subOne (tuple of matching start positions of sub_string1), 
               subTwo(tuple of matching start positions of sub-string 2) and len_sub_str_One (length of first sub-string)
    Return: Tuple of fuzzy matches or -1
    """
    if len(subOne) == 0 or len(subTwo) == 0:                                    # Check if one or both the tuples are empty
        return -1
    sum_pos = []                                                                # Initialize sum_pos to an empty list
    fuzzy_matches = []                                                          # Initialize fuzzy_matches to an empty list
    for pos in subOne:
        sum_pos.append(pos + len_sub_str_One + 1)                               # Append pos (position) into the list
    
    for i in range(len(sum_pos)):
        for j in range(len(subTwo)):
            if sum_pos[i] == subTwo[j]:
                fuzzy_matches.append(i)
                break
    
    subOne_list = list(subOne)
    fuzzy_only_matches = [i for i in subOne_list if i not in fuzzy_matches]     # Iterate through subone_list and remove fuzzy matches
    return tuple(fuzzy_only_matches)                                            # return tuple of fuzzy only matches


def fuzzyMatchesOnly(srch_str, sub_str):
    """
    Purpose: Find fuzzy matches which are not an exact match
    Arguments: srch_str (string searched) and sub_str (sub-string to search)
    Return: Tuple of fuzzy matches or -1
    """
    if len(srch_str) == 0 or len(sub_str) == 0:                                 # Check if both the strings are input by the user
        return -1
    sub_str1, sub_str2 = random_split(sub_str)
    if (sub_str1 == None or sub_str2 == None):
        return -1
    matched_indices1 = allMatchedIndices(srch_str, sub_str1)                    # Get matched indices for sub-string 1
    matched_indices2 = allMatchedIndices(srch_str, sub_str2)                    # Get matched indices for sub-string 2

    return fuzzyMatching(matched_indices1, matched_indices2, len(sub_str1))


# Main program for debugging
"""
search_string = input("Enter search string: ")
sub_string = input("Enter sub-string to be searched: ")
fuzzy_matches = fuzzyMatchesOnly(search_string, sub_string)
if fuzzy_matches != -1:
    print(fuzzy_matches)
"""