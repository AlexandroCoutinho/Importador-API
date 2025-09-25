"""
Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.
"""

available_money = 50
product_price = 15
product_tax = 0.03
result = available_money - (product_price + (product_price * product_tax))
print(result)

