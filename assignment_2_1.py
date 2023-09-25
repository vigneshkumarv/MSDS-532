"""
Assignment 2_1: Script to find 450th prime number
September 13, 2023
Vignesh Kumar Venkateshwar
"""
from math import sqrt

# Function to verify if input is prime or not
def IsPrime(input_num):
    i = 2
    count = sqrt(input_num)
    while i <= count:
        if(input_num % i == 0):
            return 0
        i+=1
    if i > count:
        return 1


prime_to_find = 450  # Prime number to find (450th in this case)
prime_count = 0      # Initializing prime_count to zero
prime_list = []      # Initializing empty list called prime_list to store primes

odd_numbers = [odd for odd in range (3, 4000, 2)]  # Create a list of odd numbers until 4000
# Since 2 is the only even prime, appending it to prime list first
prime_list.append(2)
prime_count+=1

# Logic to check if odd input from odd_numbers list is prime or not and appending it to prime_list
for test_input in odd_numbers:
    if(IsPrime(test_input)):
        prime_list.append(test_input)
        prime_count+=1
        if(prime_count % 50 == 0):
            print("{} prime numbers so far".format(prime_count))
            print(prime_list)
        if prime_count == prime_to_find:
            print("The {}th prime number is {}".format(prime_to_find, test_input))
            break
