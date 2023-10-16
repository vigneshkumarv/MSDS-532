"""
Assignment 5 Problem 1: use successive approximation to find
the value of an investment given salary, savings, rate and
duration
October 3, 2023
Vignesh Kumar Venkateshwar
"""

def fixedInvestor(salary, p_rate, f_rate, years):
    """
    Purpose: To determine amount obtained at retirement based on investment
    Arguments: salary, p_rate (personal investment rate), f_rate (fixed growth rate) & years
    Return: List comprising total value of retirement plan at the end of each year or -1
    """
    if (salary < 0 or p_rate < 0 or f_rate < 0 or years < 0):               # Check if any of the function parameters are negative
        return -1
    retirement_amount = []                                                  # Initialize an empty list to store the result
    if p_rate < 5:
        match_rate = p_rate/100                                             # If personal investment rate is less than 5%, use it as match rate
    else:
        match_rate = 5/100                                                  # If personal investment rate is greater than 5%, cap match rate to 5%
    per_rate = p_rate/100
    amount = 0
    for year in range(years):
        amount *= (1 + f_rate/100)                                          # Calculate growth rate amount
        amount += (salary * (0.05 + per_rate + match_rate))                 # Calculate successive approximation amount
        retirement_amount.append(round(amount, 2))                          # Append calculated amount (rounded off to two decimal places) into the list
    
    return retirement_amount


# Main program for debugging
"""
sal = int(input("Enter Salary: "))
p_r = int(input("Enter your preferred interest rate: "))
f_r = int(input("Enter growth rate: "))
yrs = int(input("Enter no. of years of investment: "))
print(fixedInvestor(sal, p_r, f_r, yrs))
"""