# Author = Darren Isaacson
# This prorgram is designed to calculate the sales tax of the users purchase

print("Welcome to the sales tax calculator\n")

# Enter in there purchase value
userPurchase = float(input("What was your total purchase today? "))

#Foundating the sales tax to variables
stateTax = 0.05
countyTax = 0.025

# Finding the tax difference and putting them into variables
stateTaxtotal = stateTax * userPurchase
countyTaxtotal = countyTax * userPurchase

# Calculating the total tax
salesTaxtotal = countyTaxtotal + stateTaxtotal

# Calculating the total cost of the purchase with tax
totalCost = salesTaxtotal + userPurchase

# Creating a formated output
print("Your total is going to be: $" + format(totalCost,'.2f'))
print("Here is the serperation of your purchase today!\n")

# Creating a formated table
print("Price\tState Tax\tCounty Tax\tTotal")
print("$" + format(userPurchase,'.2f') + "\t$" + format(stateTaxtotal,'.2f') + "\t\t$" +
      format(countyTaxtotal,'.2f') + "\t\t$" + format(totalCost,'.2f')
)
print("\nThanks for Shopping!")
