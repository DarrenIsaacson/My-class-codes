# Author = Darren
# This program is designed to calculate and display the average quiz score
# each student who takes a number of quizzes.

def main():
    print("Welcome to the test average calculator! \n---------------------------------------")

    # This will help formulate the exemptions
    try:

        # Creates variables for the input values funtion
        numStudents, numQuiz = getInput()

        # For loop 
        for student in range(1, numStudents + 1): # Adding 1 because binary code sets 1 to 0
            
            average = getAverage(numQuiz) # Sending values to average

            printOutput(average, student) #Sending formula to print statement

        print("---------------------------------------\nThanks for using the program")            


    # General exemption
    except:
        print("There was an error. Please try again.")
        

def getInput():

    # Asks the user for students and quizzes taken
    getStudents = int(input("How many students do you want to calculate? :"))
    getQuiz = int(input("How many quizzes were taken for each student? :"))

    # Returns student input and quiz input back to main()
    return getStudents, getQuiz


def getAverage(quiz):

    
    total = 0

    # Loop for collecting quiz scores and averaging them out
    for num in range(quiz):

        # Input variable for collecting the scores
        score = float(input("What was the score of test number %d?" % (num + 1)))

        total = total + score   # Base accumulator

        average = total/quiz    # Calculation to find average

    # Returns average value back to main()
    return average

def printOutput (average, student):

    # Used python shortcuts to display which student and their average
    print("The average for student %d is: %.2f." % (student, average))

main()


