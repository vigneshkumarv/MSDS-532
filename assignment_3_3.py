"""
Assignment 3 Problem 3: Provide least expensive option along with total cost for quantity of chicken nuggets ordered
September 23, 2023
Vignesh Kumar Venkateshwar
"""

# Global variables
max_order = 1850        # Maximum quanity that can be ordered
min_cost = 800          # Minimum cost (3 * 50 + 4 * 50 + 9 * 50)
min_diff = 6            # Minimum difference between requested number of nuggets and availability
order_feasible = False  # Flag to check if the order is feasible
nuggets_order = {}      # Dictionary to hold different quantities of nuggets
order_list = []         # List to hold different order options
u_a = 0                 # Variable which represents quantity of boxes of 6 nuggets (6 * u_a)
u_b = 0                 # Variable which represents quantity of boxes of 9 nuggets (9 * u_b)
u_c = 0                 # Variable which represents quantity of boxes of 22 nuggets (22 * u_c)


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
                elif res != 0 and abs(res - num) < min_diff:
                    globals()["min_diff"] = abs(res - num)
                    globals()["u_a"] = a
                    globals()["u_b"] = b
                    globals()["u_c"] = c
                    break


# Function to evaluate cost
def evaluate_cost(list_input):
    for index, option in enumerate(list_input):
        cost = 3 * option["Six_piece"] + 4 * option["Nine_piece"] + 9 * option["Twenty_two_piece"]
        if cost < globals()["min_cost"]:
            min_index = index
            globals()["min_cost"] = cost
    print("The least expensive option available at ${} is: ".format(globals()["min_cost"]))
    print(list_input[min_index])


# Main program
order_input = int(input("How many chicken nuggets would you like to order (MAX:{})? ".format(max_order)))
if order_input < 1 or order_input > max_order:
    print("Sorry! your order cannot be processed, please enter a valid number")
else:
    evaluate_order(order_input)
    if order_feasible:
        evaluate_cost(order_list)
    else:
        print("Sorry! Requested quantity cannot be ordered")
        updated_quantity = 6 * u_a + 9 * u_b + 22 * u_c       # Calculate updated quantity from values of u_a, u_b and u_c
        evaluate_order(updated_quantity)
        evaluate_cost(order_list)