# Author = Darren Isaacson
# This program is designed to create mix colors based off what the user has for colors.

#This allows the user to choose 2 colors
color1 = input("Choose a color between red, blue, and yellow to mix. ")

color2 = input("Choose another color you want to mix between red, blue, and yellow. ")


# Red + Yellow = Orange
if color1 == "red" and color2 == "yellow" or color1 == "yellow" and color2 == "red" :
    # Displays color
    print("The results of the mix is: Orange!")
# Red + Blue = Purple
elif color1 == "red" and color2 == "blue" or color1 == "blue" and color2 == "red" :
    print("The results of the mix is : Purple!")
# Red + Red = Red
elif color1 == "red" and color2 == "red":
    print("The results of the mix is : Red!")
# Blue + Yellow = Green
elif color1 == "blue" and color2 == "yellow" or color1 == "yellow" and color2 == "blue" :
    print("The results of the mix is : Green!")
# Blue + Blue = Blue
elif color1 == "blue" and color2 == "blue" :
    print("The results of the mix is : Blue!")
# Yellow + Yellow = Yellow
elif color1 == "yellow" and color2 == "yellow" :
    print("The results of the mix is : Yellow!")
# Error for any other colors that were not listed
else :
    print("Error! You tried unavailble colors.")

print("End of program")
