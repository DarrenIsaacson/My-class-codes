# Author = Darren Isaacson
# This program is designed to accumulate the users numbers chosen

# Users input for base and upper values
baseNumber = int(input("What is your base number? :"))
upperNumber = int(input("What is your upper number? :"))

# Total baseline for accumulator
total = 0

# For loop variant
for number in range(baseNumber, upperNumber + 1):
    print(number) # prints the accumlation
    total = total + number

# prints total
print("The total amount is : %d" % total)
