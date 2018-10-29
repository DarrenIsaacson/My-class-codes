# Author = Darren Isaacson
# This program is desiged to calcualthe the tax, tip, and total for a meal in a
# resturant.

# Global variable for tax
taxRate = .075

# 2 input variable that are collected from the user
getAmount = float(input("What was the cost of your food?"))
getPercentage = float(input("Enter in a tip percentage that you would like to give"))

# Multiply tip amount to total
tip = getPercentage * getAmount

# Multiply tax amount to total
tax = getAmount * taxRate

# Collect all values and add the together for the total
total = getAmount + tip + tax

# Print output
print("The total of your meal today is $%.2f" %total)
