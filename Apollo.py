# Author = Darren Isaacson
# This program is designed to define if a question is right or wrong

# This function asks the question
year = int(input("When did Apollo 11 land on the moon"))

# This defines if the answer from the input was correct
if year == 1969 :
    print("Correct!")
else :
    print("Sorry, wrong answer")

print("End of program")








# This function is a variation of the first code

# This function asks the user for a number question
year = int(input("When did Apollo 11 land on the moon?"))

# This if the answer is not 1969 then it is wrong
if year != 1969 :
    print("Sorry, wrong answer")

# Any other answer is right
else :
	print("Correct!")
