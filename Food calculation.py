# Author = Darren Isaacson
# This program is designed to calculate the total cost of meal.

print("Thank you for dining with us today \n------------------------------------")

tax = 1.075

costofMeal = float(input("What was the cost of your meal?\n$"))

getTip = float(input("Would you like to leave a tip? Enter in a tip value if so:"))


if getTip >= 0:
    getTip = 0
else:
    getTip = 0
    


taxTotal = costofMeal * tax
fullTotal = taxTotal + getTip


print("------------------------------------")
                   
print("Food: $%.2f" % taxTotal)
print("Tip: $%.2f" % getTip)
print("Total = $%.2f" % fullTotal)
