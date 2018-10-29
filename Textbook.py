# Author = Darren Isaacson
# This program is designed to calculate the total cost of books purchased

# While loop variant
books = int(input("How many textbooks? "))
total = 0.0
bookCount = 1
while bookCount <= books :	# test the condition
	price = float(input("Enter price of book %d: " % bookCount))  
	total = total + price
	bookCount = bookCount + 1		# add 1 to the bookCount
print("All the books cost $%6.2f" % total)

# For loop variant
books = int(input("How many textbooks did you buy this semester?"))
moneySpent = 0.0
for number in range(books):     # "5" will not be included, it will reach "4"
    bookPrice = float(input("Type a textbook price: " + str(number + 1)))
    moneySpent = moneySpent + bookPrice
    
# Formmated with condition shorcuts 
print("Total spend = $%0.2f" % moneySpent)
