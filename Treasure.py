print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')
print("\nWelcome to Treasure Island.\nYour mission is to find the treasure.\nYou are walking and there are two paths infront of you!\n")
path = input("Which path would you like to pick? L or R?\n").capitalize()
if path == "L":
    print("Congrats you chosed the right path, but you bumped into a lake. You can't go around it.")
    swim = input("Are you going to swim across or are you going to wait for a boat? S or W?\n").capitalize()
    if swim == "W":
        print("You crossed the lake safely. On the otherside of the lake there is a house with three doors a blue and a red and a yellow.")
        door = input("Which door would you like to pick? B or R or Y?\n").capitalize()
        if door == "B":
            print("You were eaten by cannibals. Game over.")
        elif door == "R":
            print("Congratulations, YOU FOUND THE TRESURE. You just became a billioner! Unfortunatelly, it was guarded by dragons so you died. Game over.")
        else:
            print("The door closed behind you and you could not open it. You starved to death. Game over")
    else:
        print("You got stung buy a poisinous jellyfish and you didn't make it to the other side. Game over.\n")
else:
    print("You fell into a hole. Game over.")


