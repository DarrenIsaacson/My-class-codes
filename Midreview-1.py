# Author = Darren Isaacson
# This program is designed to calculate the total cost of meal.

print("Thank you for dining with us today \n------------------------------------")

# Global tax varible
tax = 1.075

# Input of Food
costofMeal = float(input("What was the cost of your meal?\n$"))

# Input validation for food cost
if costofMeal <= 0:
    costofMeal = 0
    
else:
    costofMeal = costofMeal

# Input for Tip
getTip = float(input("Would you like to leave a tip? Enter in a tip value if so:"))

# Validation for tip

if getTip <= 0:
    getTip = 0
    
else:
    getTip = getTip
    

# Calculations
taxTotal = costofMeal * tax
fullTotal = taxTotal + getTip


# Output
print("------------------------------------")
                 
print("Food: $%.2f" % taxTotal)
print("Tip: $%.2f" % getTip)
print("Total = $%.2f" % fullTotal)
