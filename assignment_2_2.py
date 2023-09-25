"""
Assignment 2_2: Script to verify if sum of logarithms of primes converge to input n
September 13, 2023
Vignesh Kumar Venkateshwar
"""
import sys
from math import *

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


prime_log = [] # Initialize empty list to store logarithms of primes
start = 2
n = int(input("Please input n: "))
# Handle user inputs less than 2
if n < 2:
    sys.exit("Invalid n, please enter n greater than 2")

while start < n:
    if(IsPrime(start)):
        prime_log.append(log(start))
    start+=1

sum_of_prime_log = sum(prime_log) # Calculate sum of logarithms of primes
ratio = sum_of_prime_log / n      # Calculate ratio of sum of logarithms of prime and n
print("Sum of logarithms of primes: {0}, n: {1}, ratio: {2}".format(sum_of_prime_log, n, ratio))
