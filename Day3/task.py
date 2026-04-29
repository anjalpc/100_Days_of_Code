print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road = input('You\'re at a cross road. Where do you want to go?\n').lower()
# add backslash to eliminate " ' closing the string early. Add .lower() without space to convert the input to lower case
if road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    do = input('Type "swim" to swim to the island or "wait" to wait for a boat\n').lower()
    if do == "wait":
        print("You've reached the Island. In front you find 3 doors, Red, Blue and Yellow")
        colour = input('Type "red" to go through the red door,'
                       ' "yellow" to go through the yellow door and "blue" to go through the blue door\n').lower()
        if colour == "red":
            print("You got burned by fire. GAME OVER.")
        elif colour == "yellow":
            print("YOU FOUND THE TREASURE")
        elif colour == "blue":
            print("You are eaten by beasts. GAME OVER.")
        else:
            print("GAME OVER")
    else:
        print("You got attacked by trout. GAME OVER.")
else:
    print("You fell into a hole. GAME OVER.")
