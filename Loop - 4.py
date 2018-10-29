# Author = Darren Isaacson
# This program is designed to accumulate 2 input values and make a list.

# This is the cordinator of the other functions
def main():
    print("Welcome to the looping program \n---------------------------------------")

    # Try statement goes first to startup exceptions
    try:
        # Collects small and large for input values
        small,large = getNumber()
        
        # Sends input values to calculate
        answer, list = calculate(small,large)
        
        # Sendsing total accumulation and list to outputAnswer
        outputAnswer(answer,list)
        
    # Generic exception 
    except:
        print("Error! Please try again.")

# This function gathers the values from the user
def getNumber():

    # Collects information from the user
    getSmall = int(input("Enter in your small number. :"))
    getLarge = int(input("Enter in your large number. :"))
    # Returns input values
    return getSmall, getLarge

# This function calculates the numbers in range
def calculate(small, large):

    list = []    
    total = 0
    # This for stament is only for accumulating the varibles 
    for number in range(small,large+1):
        list.append(number)     # This adds to the list for every int being added from the loop
        total = total + number  # This accumulates the value
    # Return accumulator total and list values
    return total, list

# This function displays the output
def outputAnswer(answer,list):
    print("The total is :%d " % answer)
    print("Your list of numbers is",list)
    print("---------------------------------------")



main()
