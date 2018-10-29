# Author = Darren Isaacson
# This program is designed

# Asks the user how much money they have
money = int(input("What is the total amount of cents do you have"))

# Defines if the user has more, less, equal, or no money and displays output
if money > 100 :
    print("You have more than a dollor")
elif money == 100 :
    print("You have exactly a dollar")
else:
    print("You have less than a dollar")


print("End of program")
