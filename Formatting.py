# Author = Darren Isaacson
# This program is designed to test formats

usersName = "Darren"
print("Hello %s, it's nice to meet you\n" % usersName)

temp = 67
print("Today's temperature was %d Fahrenheit\n" % temp)


students = 30
assignments = 20
missing = students - assignments
print("I have %d students but only %d assignments so I'm missing %d\n" % (students, assignments, missing))

temp = 90
food = "ice cream"
# This works
print("Today it is %d F. I'm going to eat some %s." % (temp, food))
# This format is flipped at the end
doesnotWork = print("print(\"Today it is %s F. I'm going to eat some %d.\" % (temp, food)"
                    "\n does not work because of formation of the int and string variation\n")

import math
divided = 100.0 / 3.0
print ("$100 divided by 3 is $%3.2f" % divided)
print ("The value of pi to 4 decimal places is %1.4f\n" % math.pi)

print('Here is the 12 times table')
for number in range(13):
    print('%d times 12 is %d' % (number, number*12))



mult = 12
print('Here is the 12 times table')
for number in range(13):
    # This variable need to be in the loop to function.
    result = number * mult 
    print('%d times 12 is %d' % (number, result))
