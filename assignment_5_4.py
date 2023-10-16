"""
Assignment 5 Problem 4: Calculate maximum annual expense amount to use up all of the retirement savings
October 8, 2023
Vignesh Kumar Venkateshwar
"""

def calculate_retirement_value(saved, retiredRate, expense):
    """
    Purpose: To calculate the retirement value
    Arguments: saved amount, retiredRate (list of annual interest rate on retirement) and expense
    Return: remaining retirement amount value
    """
    remaining_value = saved                                                                              # Set remaining_value as saved (principal amount)
    for index in range(len(retiredRate)):                                                                # Calculate remaining amount value based on expense and retired rate
        remaining_value -= expense                                                                     
        remaining_value += remaining_value * (retiredRate[index]/100)
    
    return remaining_value


def maximumExpensed(salary, p_rate, workRate, retiredRate, epsilon):
    """
    Purpose: To calculate maximum amount that can be expensed every year until all of the retirement savings are used up
    Arguments: salary, p_rate (personal investment rate), workRate (list of annual interest rate when working),
    retiredRate (list of annual interest rate on retirement) and epsilon
    Return: final expense or -1
    """
    if (salary <= 0 or p_rate < 0 or len(workRate) == 0 or len(retiredRate) == 0 or epsilon < 0):        # Check if any of the function parameters are zero/negative
        return -1
    if p_rate < 5:
        match_rate = p_rate/100                                                                          # If personal investment rate is less than 5%, use it as match rate
    else:
        match_rate = 5/100                                                                               # If personal investment rate is greater than 5%, cap match rate to 5%
    per_rate = p_rate/100
    retirement_amount = 0
    for index in range(len(workRate)):                                                                   # Calculate retirement amount for no. of years worked
        retirement_amount *= (1 + workRate[index]/100)
        retirement_amount += (salary * (0.05 + per_rate + match_rate))
    
    lower_limit = 0                                                                                      # Initilize lower limit to zero
    upper_limit = salary * len(retiredRate) * 2                                                          # Initilize upper limit to a ballpark value

    # Binary Search
    while upper_limit - lower_limit > epsilon:
        expense_amount = (upper_limit + lower_limit) / 2
        retirement_value = calculate_retirement_value(retirement_amount, retiredRate, expense_amount)    # Calculate retirement amount value based on expense amount

        if retirement_value < 0:
            upper_limit = expense_amount
        else:
            lower_limit = expense_amount

        print(f"Expense Amount: ${expense_amount:.2f}, Remaining Value: ${retirement_value:.2f}")

    final_expense = (upper_limit + lower_limit) / 2                                                      # Calculate final annual expense amount                                                
    final_remaining_value = calculate_retirement_value(retirement_amount, retiredRate, final_expense)    # Calculate final remaining value
    print(f"Final Expense: ${final_expense:.2f}, Final Remaining Value: ${final_remaining_value:.2f}")
    
    return final_expense


# Main program for debugging
"""
sal = int(input("Enter Salary: "))
p_r = int(input("Enter your preferred interest rate: "))
yrs = int(input("Enter no. of years of investment: "))
w_r = []
for yr in range(yrs):
    int_rate = int(input("Enter interest rate for year {}: ".format(yr+1)))
    w_r.append(int_rate)
r_r = []
yrs = int(input("Enter no. of years of retirement: "))
for yr in range(yrs):
    int_rate = int(input("Enter interest rate for year {}: ".format(yr+1)))
    r_r.append(int_rate)
eps = float(input("Enter Epsilon: "))
result = maximumExpensed(sal, p_r, w_r, r_r, eps)
print(f"The maximum expense during retirement is ${result:.2f}")
"""