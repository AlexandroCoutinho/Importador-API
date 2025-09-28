"""
Functions
"""

print("Hello and welcome to functions!")


def print_my_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}.")

def print_color_red():
    color = "Red"
    print(color)

def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)

def multiply_numbers(a, b):
    result = a * b
    return result

def print_list(list):
    for x in list:
        print(x)

def buy_item(cost_of_item):
    return cost_of_item+ add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate

final_cost= buy_item(50)
print(final_cost)
