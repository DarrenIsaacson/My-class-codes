# Author = Darren Isaacson
# This program is designed to help create list and calculate the values.

def main():

    try:
        values = getValues()# Gathers list values

        count,list,total = listOutput(values) # Accumulates the values

        printOutput(list,total) #Prints output

    # General Exceptions
    except:
        print("There was an error")




def getValues():

    
    valueList = [] #Base list
    go = "y" # Base variable
    num = 0 # Base value accumulator
    while go == 'y': # While loop for input value
        values = float(input("What is the pricing for values #%d" %(num + 1)))
        while values <=0:
            values = float(input("Values must be greater that 0. What is the pricing for values #%d" %(num + 1)))
        valueList.append(values) # Collects values inputed
        num += 1

        go = input("Do you want to enter another value? Press y to enter another value or any other key to stop") # Loop break

    return valueList


def listOutput(values):

    
    total = 0
    
    for count in range(len(values)): # Takes each value in list
        total = total + values[count]  # List accumulator

    return count, values, total



def printOutput(list,total):

    for x in list:
        print("Value numbers in your list are %.2f" % x) # Displays each value in list

    print("The total of your list is: $%.2f" % total) # Displays total

main()
