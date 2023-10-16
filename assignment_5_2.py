"""
Assignment 5 Problem 2: use successive approximation to find
the value of an investment given salary, savings, and variable growth rate
October 4, 2023
Vignesh Kumar Venkateshwar
"""

def variableInvestor(salary, p_rate, v_rate):
    """
    Purpose: To determine amount obtained at retirement based on investment
    Arguments: salary, p_rate (personal investment rate), & v_rate (variable growth rate)
    Return: List comprising total value of retirement plan at the end of each year or -1
    """
    if (salary < 0 or p_rate < 0 or len(v_rate) == 0):                 # Check if salary/p_rate is negative or length of v_rate list is zero
        return -1
    retirement_amount = []                                             # Initialize an empty list to store the result
    if p_rate < 5:
        match_rate = p_rate/100                                        # If personal investment rate is less than 5%, use it as match rate
    else:
        match_rate = 5/100                                             # If personal investment rate is greater than 5%, cap match rate to 5%
    per_rate = p_rate/100
    amount = 0
    for index in range(len(v_rate)):
        amount *= (1 + (v_rate[index]/100))                            # Calculate growth rate amount based on variable rate
        amount += (salary * (0.05 + per_rate + match_rate))            # Calculate successive approximation amount
        retirement_amount.append(round(amount, 2))                     # Append calculated amount (rounded off to two decimal places) into the list

    return retirement_amount


# Main program for debugging
"""
sal = int(input("Enter Salary: "))
p_r = int(input("Enter your preferred interest rate: "))
yrs = int(input("Enter no. of years of investment: "))
v_r = []
for yr in range(yrs):
    int_rate = int(input("Enter interest rate for year {}: ".format(yr+1)))
    v_r.append(int_rate)
print(variableInvestor(sal, p_r, v_r))
"""