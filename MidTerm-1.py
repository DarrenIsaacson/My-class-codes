# Author = Darren Isaacson
# This program is designed to cakcukate and display the information for a one way flight
# to New Zealand.

print("Welcome to D Airline agent")
print("This trip is going to New Zealand today! \n---------------------------------------------")
# Global Variables
ticketPrice = 1500
suitcasePrice = 40
taxandFees = 500
singleAgent = 75

# Collects user quanities
getticketQuanity = int(input("How many tickets will you be needing?"))
getsuitcaseQuanity = int(input("How many suitcases are you bringing?"))

#Calculates the quanities by the cost of tickets, suitcases, fees, and agent
suitcaseCost = suitcasePrice * getsuitcaseQuanity
ticketCost = (ticketPrice + taxandFees) * getticketQuanity
total = suitcaseCost + ticketCost + singleAgent

# Prints output
print("Cost per ticket: $%.2f" % ticketPrice)
print("Cost per suitcase: $%.2f" % suitcasePrice)
print("Tax and Fees per ticket: $%.2f" % taxandFees)
print("Agent fee: $%.2f" % singleAgent)
print("Suitcase Total: $%.2f" % suitcaseCost)
print("Ticket Total: $%.2f" % ticketCost)
print("Total: $%.2f" % total)

