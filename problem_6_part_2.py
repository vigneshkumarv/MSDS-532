"""
Assignment 6 Part 2: Creating a two-player word game similar to Ghost
October 15, 2023
Vignesh Kumar Venkateshwar
"""
import random

letters = "abcdefghijklmnopqrstuvwxyz"

# -----------------------------------
# Helper functions
# (you don't need to understand this code)

wordlist_file = "words.txt"

def import_wordlist():
    """
    Imports a list of words from external file
    Returns a list of valid words for the game
    Words are all in lowercase letters
    """
    print("Loading word list from file...")
    with open(wordlist_file) as f:                        # call file, read file to list
        wordlist = [word.lower() for word in f.read().splitlines()]
    print("  ", len(wordlist), "words loaded.") 
    return wordlist


def into_dictionary(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# end of helper functions
# -----------------------------------

def validate_letter(letter):
    """
    Purpose: To validate if the input letter is valid or not
    Arguments: Letter (character)
    Return: True/False
    """
    if letter not in letters or len(letter) != 1:                   # Check if letter is in letters and its no longer than one character
        return False
    return True


def substring_validity(substring, wordlist, letter):
    """
    Purpose: To validate if the sub-string fragment is valid or not
    Arguments: substring, wordlist (list of valid words) and letter (character)
    Return: True/False
    """
    if substring == "":                                             # Check if substring is empty
        return True
    new_substring = substring + letter                              # Append letter to substring
    if len(new_substring) > 3 and new_substring in wordlist:        # Check if new_substring is longer than three characters and forms a valid word
        return False
    for word in wordlist:                                           # Iterate through list of words and check if word starts with the new_substring
        if word.startswith(new_substring):
            return True
    return False


def get_player_input(player, word_fragment, wordlist):
    """
    Purpose: To obtain player input and verify if its valid or not
    Arguments: Player (1 or 2), word_fragment and wordlist
    Return: new word fragment if valid or else -1
    """
    print("The current word fragment is: {}".format(word_fragment))                     # Display current word fragment
    player_input = input("{}, please enter your preferred letter:\n".format(player))    # Get player input (character)
    while validate_letter(player_input) != True:                                        # Give player multiple attempts to input a valid character
        print("Invalid input, please try again")
        player_input = input()
    if substring_validity(word_fragment, wordlist, player_input):                       # Check if substring with appended letter (character) is valid
        word_fragment = word_fragment + player_input                                    # Update word fragment by appending player input
        return word_fragment
    else:
        return -1


def play_game(wordlist):
    """
    Purpose: Method to play the actual game
    Arguments: wordlist (list of valid words)
    Return: None
    """
    current_string = ""
    player_1 = input("Player 1, please enter your name:\n")                             # Get name of player 1
    player_2 = input("Player 2, please enter your name:\n")                             # Get name of player 2
    while True:
        player_1_input = get_player_input(player_1, current_string, wordlist)           # Get player 1 input
        if player_1_input == -1:                                                        # If get_player_input method returns -1, player 1 loses the game
            print("{}, you lost the game!".format(player_1))
            break
        else:
            current_string = player_1_input                                             # Update current string with player 1 input if valid                     
        player_2_input = get_player_input(player_2, current_string, wordlist)           # Get player 2 input
        if player_2_input == -1:                                                        # If get_player_input method returns -1, player 2 loses the game
            print("{}, you lost the game!".format(player_2))
            break
        else:
            current_string = player_2_input                                             # Update current string with player 2 input if valid
    print("Game Over!")


# Load the word dictionary by assignment the file name to 
# the wordlist variable 
wordlist = import_wordlist()
play_game(wordlist)
