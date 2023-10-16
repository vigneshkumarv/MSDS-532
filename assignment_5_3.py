"""
Assignment 5 Problem 3: Calculate annual change of principal amount post retirement
October 4, 2023
Vignesh Kumar Venkateshwar
"""

def finallyRetired(saved, v_rate, expensed):
    """
    Purpose: To determine annual change of principal amount post retirement
    Arguments: saved, v_rate (variable annual interest rate) & expensed (annual expense)
    Return: List comprising annual value of principal amount or -1
    """
    if (saved <= 0 or len(v_rate) == 0):                        # Check if saved amount is less than or equal to zero OR length of list v_rate is zero
        return -1
    principal_amount = []                                       # Initialize principal amount to an empty list
    amount = saved
    for i_rate in v_rate:
        amount -= expensed                                      # Subtract annual expense
        if amount > 0:
            amount += (amount * (i_rate/100))                   # Calculate interest amount and add it to principal amount
            principal_amount.append(round(amount, 2))           # Append calculated amount to the list
        else:
            principal_amount.append(0)                          # Append zero to the list if principal amount becomes less than zero
    
    return principal_amount


# Main program for debugging
"""
sav = int(input("Enter Saved amount: "))
exp = int(input("Enter your annual expense: "))
yrs = int(input("Enter no. of years of investment growth: "))
v_r = []
for yr in range(yrs):
    int_rate = int(input("Enter interest rate for year {}: ".format(yr+1)))
    v_r.append(int_rate)
print(finallyRetired(sav, v_r, exp))
"""