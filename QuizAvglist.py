# Author = Darren Isaacson
# This program is designed to create a list for the students and calculate the total

def main():
  
    try:

        numStudents, numQuiz = getInput()
        classlist = studentLoop(numStudents,numQuiz)
        average = totalclassAVG(classlist)
        classaverageOutput(average)

    # General exemption
    except:
        print("Error somewhere in the program")
   
        
def getInput():

    # Asks the user for students and quizzes taken
    getStudents = int(input("How many students do you want to calculate? :"))
    getQuiz = int(input("How many quizzes were taken for each student? :"))

    # Returns student input and quiz input back to main()
    return getStudents, getQuiz


def studentLoop(numStudents, numQuiz):
    # Add blank list
    classlist = []
    for student in range(1, numStudents + 1): # Adding 1 because binary code sets 1 to 0
        average, list = getQuiz(numQuiz) # Function to collect average test
        classlist.append(average) # Add average to the "classlist" list
        printOutput (list, average, student)
    return classlist
        
        


def getQuiz(quiz):
    # Add blank list
    list = []
    total = 0
    for num in range(quiz):
        score = float(input("What was the score of test number %d?" % (num + 1)))
        list.append(score) # Add each input score into a list for further diplay
        total = total + score   # Base accumulator
        average = total/quiz
    return average, list
        
def getList(Quiz):
    
    total = 0 
    for loop in range(Quiz):
       score = float(input("What was the score of test number %d?" % (num + 1)))
       list.append(score)
       total = total + score   # Base accumulator
       average = total/Quiz    # Calculation to find average
    return list, average



def printOutput (list, average, student):

    # Used python shortcuts to display which student and their average
    print("The average for student %d is: %.2f." % (student, average))
    print("Student test list:", list)




def totalclassAVG(classlist):
    # Create base total
    total = 0
    for x in range(len(classlist)):
        # Takes lenth of 'classlist' list and calculates the total
        total = total + classlist[x]
    # Divides the total by the amount numbers in the list
    average = total/len(classlist)
    return average 



def classaverageOutput(average):
    # Print class average
    print("Average class total is %.2f" % average)



main()
                                                    
