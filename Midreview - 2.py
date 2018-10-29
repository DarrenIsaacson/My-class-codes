# Author = Darren Isaacson
# This program is designed to calulate the amount of widgets being purchased and discount them based off quantity.

def main ():
    
    # Try function to startup excemptions
    try:
        # Global cost for widgets
        cost = 99.00

        
        quantity = getQuantity() # Collect user input
        discount, quantity = getDiscount(quantity) # Collects discount
        total = getCalculations(discount, quantity, cost) # Collects total
        printOutput(total) # Sends output

    except: # Adds excemption for letters
        print("There is an Error! You cannot enter letters or special characters. Please reopen the program and try again.")



def getQuantity ():
    
    # User input variable    
    quantity = int(input("How many widgets would you like to purchase?"))

    # Data validation for users to change negative value to 0.
    if quantity < 0:
        quantity = 0

    else:
        quantity = quantity


    return quantity # Return amount quantity



def getDiscount(amountofProducts):

    # Loop statment to collect discount value
    if amountofProducts <= 9:
        discount = 1.0

    elif amountofProducts <= 19:
        print("You will recieve a 10% discount")
        discount = .9
        
    elif amountofProducts <= 49:
        print("You will recieve a 20% discount")
        discount = .8
        
    elif amountofProducts <= 99:
        print("You will recieve a 30% discount")
        discount = .7
    else :
        print("You will recieve a 40% discount")
        discount = .6

    return discount, amountofProducts

def getCalculations(discount,quantity,cost):

    # This calculates the base value
    baseCost = quantity * cost

    #This calculates and converts the discounte value if there is one
    discountCost = baseCost * discount


    print("You saved: $%.2f" % (baseCost - discountCost))

    return discountCost


def printOutput(total):

    # This prints values associated with the remaining value
    print("You total amount is $%.2f" % total)


main()
