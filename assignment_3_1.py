"""
Assignment 3 Problem 1: Find quantity of chicken nuggets that fit within available order quantities
September 22, 2023
Vignesh Kumar Venkateshwar
"""

# Global variables
max_order = 1850        # Maximum quanity that can be ordered
order_feasible = False  # Flag to check if the order is feasible
nuggets_order = {}      # Dictionary to hold different quantities of nuggets
order_list = []         # List to hold different order options


# Function to evaluate order
def evaluate_order(num):
    for a in range(51):
        for b in range(51):
            for c in range(51):
                res = 6 * a + 9 * b + 22 * c
                if res == num:
                    globals()["order_feasible"] = True          # Setting global flag to True
                    nuggets_order["Six_piece"] = a
                    nuggets_order["Nine_piece"] = b
                    nuggets_order["Twenty_two_piece"] = c
                    order_list.append(nuggets_order.copy())     # Appending copy of nuggets_order to prevent it from being overwritten
                    break


# Main program
order_input = int(input("How many chicken nuggets would you like to order (MAX:{})? ".format(max_order)))
if order_input < 1 or order_input > max_order:
    print("Sorry! your order cannot be processed, please enter a valid number")
else:
    evaluate_order(order_input)
    if order_feasible:
        print("For an order size of {}, choose from the following {} option(s):".format(order_input, len(order_list)))
        for option in order_list:
            print(option)
    else:
        print("Sorry! Requested quantity cannot be ordered")
