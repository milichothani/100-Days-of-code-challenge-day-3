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
choice = input("You\'re at cross road. Where do you want to go? \n Type "'left'" or "'right'" ")
if choice == "right":
    print("OOOPS! you were taken by a tiger. GAME OVER!!")
elif choice == "left":
    print("YAAY you made it to next level!!!")

    choice2 = input("Do you want to swim or wait?? \n Type "'swim'" to swim across or "'wait'" to wait for the boat: ")
    if choice2 == "swim":
        print("OOPS!! you were taken by a crocodile! GAME OVER!!!")
    elif choice2 == "wait":
        print("DAMNNN! You just made out of new challenge!!!")

        choice3 = input("Which door do you think contains treasure? \n Red, Blue or yellow? \n Type "'red'" "'Blue'" or "'yellow'": ")
        if choice3 == "red":
            print("OUCH! door contains fire!! GAME OVER!!!")
        elif choice3 == "blue":
            print("WHOOPS! door contains beast! GAME OVER!!!")
        elif choice3 =="yellow":
            print("YEAAAH! You found the door of treasure! YOU WIN!!!!")
        else:
            print("WRONG CHOICE!!! GAME OVER")

    else:
        print("OOOPS! Enter the correct input")

else:
    print("WRONG CHOICE!! GAME OVER!!! ")


