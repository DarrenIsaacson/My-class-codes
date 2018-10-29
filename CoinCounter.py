# Author = Darren Isaacson
# This program is designed to calculate the amount of money someone has and convert it into dollars

# Created base variables for coins
quarters = 25
dimes = 10
nickels = 5
pennies = 1

# Input varibles to find the how many coins for each different coin
countQuarters = int(input("How many quarters do you have? "))
countDimes = int(input("How many dimes do you have? "))
countNickels = int(input("How many nickels do you have? "))
countPennies = int(input("How many pennies do you have? "))

# Calculating the coins based off their differences
totalQuarters = quarters * countQuarters
totalDimes = dimes * countDimes
totalNickels = nickels * countNickels
totalPennies = pennies * countPennies

# Total out all the coins into a penny conversion
totalTogether = totalQuarters + totalDimes + totalNickels + totalPennies

# Created a condition based off the total amound of pennies

# Equal to a dollar
if totalTogether == 100:
    print("\nYou have exactly 1 dollar\n")
# Less than a dollar
elif totalTogether > 100:
    print("\nYou have less than a dollar\n")
# More than a dollar
elif totalTogether < 100:
    print("\nYou have more than a dollar\n")
# Anything else
else :
    print("\nYou have no money\n")

# This output is creating a table of information for the info given

print("\t\tAmount\tCount\tTotal")
print("Quarters\t" + str(quarters) + "\t" + str(countQuarters) + "\t" + str(totalQuarters))
print("Dimes\t\t" + str(dimes) + "\t" + str(countDimes) + "\t" + str(totalDimes))
print("Nickels\t\t" + str(nickels) + "\t" + str(countNickels) + "\t" + str(totalNickels))
print("Pennies\t\t" + str(pennies) + "\t" + str(countPennies) + "\t" + str(totalPennies))

# Total amount of pennies output
print("\nYou have",totalTogether,"Pennies")

print("\nEnd of program")



