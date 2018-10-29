# Author = Darren Isaacson
# This program is to practice my skills for the while loop

while True:
    print("Welcome to the coffee shop register")
    total = 0.0
    items = int(input("How many items is the customer buying?"))

    for item in range(items):
        price = float(input("Enter price of item"))
        total = total + price
    print("Total price for customer = $%4.2f" % total)

    close = input("Time to close the shop? Enter y or n:")
    if close == "y" :
        break

print("Thanks for using the program")


for count in range(5):
    print("Hello")

questions = int(input("How many questions did you ask Grumpy Cat?"))
print("This program thinks that Grumpy Cat answered as follows:")
for count in range(questions):
    print("NO.")

print("Counting program")
for number in range(10):
    print(number)

print("I can add up all the numbers between 50 and 100")
total = 0
for number in range(50, 101):
    print(number)
    total = total + number

print("The total amount of numers is %d" % total)

