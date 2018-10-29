# Author = Darren Isaacson
# This program is designed to create a personal budget list and accumulate the total

def main():
    
    # Startup try function
    try:
        print("Welcome to the value calculator, This program will help you list your values and calculate them.\n-----------------------------------------------")
        values = getValues() # Sendings input vales to collect list

        count, list, total = listOutput(values) # Sends list to calculate the total of the list

        printOutput(list,total) # Finishes the list output values
        
    except: # General output values
        print("Sorry there was an error. You cant enter and letters or special characters. Please reopen your program.")
    


def getValues():

    # Adds blank list
    valueList = []
    go = "y"
    num = 0
    # Interates values and adds them to blank list
    while go == 'y':
        values = float(input("What is the pricing for value #%d" % (num + 1)))
        while values <= 0:
            values = float(input("Value must be greater than 0. What is the pricing for value #%d" % (num + 1)))
        valueList.append(values)# Adds to the list
        num += 1 
        go = input("Do you want to enter anothe value? Press y to enter another or another key to stop")

    return valueList # Returns list to main

def listOutput(list):

    total = 0 # Set base accumulator
    for count in range(len(list)): # This loops function is to add each number in the list
        total = total + list[count]

    return count, list, total # Returns list and total back to main


def printOutput(list,total):

    for x in list: # Prints each value in list
        print("Value number in your list are %.2f" % x)
        
    print("The total of your list is: $%.2f" % total) # Prints total


main()
