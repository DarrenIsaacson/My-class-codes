# Author = Darren Isaacson
# This code will determine your grade

# Enter in score
score = float(input("Enter quiz score"))

# Generates the score grade and displays output
if score >= 90 :
    print("A grade")
elif score >= 80 :
    print("B grade")
elif score >= 70 :
    print("C grade")
elif score >= 60 :
    print("D grade")
else :
    print("You failed")

print("\nEnd of program")
