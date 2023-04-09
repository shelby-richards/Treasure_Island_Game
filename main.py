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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input("Welcome to your first choice. Left or right?")

if choice1.lower() == "left":
    choice2 = input(
        "Great choice! You live... for now. You have reached a beach. Would you like to swim or wait?"
    )

    if choice2.lower() == "wait":
        choice3 = input(
            "After waiting a while, 3 doors appear. You examine them curiously, but they reveal nothing of import besides their color: Red, Yellow, and Blue. Which door would you like to choose?"
        )
        if choice3.lower() == "red":
            print(
                "As you open the red door, a flamethrower enfulges you in flames. As you burn to a crisp, your last thought is 'I wish I had chosen a better door...' Better luck next time!"
            )
        elif choice3.lower() == "blue":
            print(
                "As you open the blue door, ravenous beasts leap through the opening and tear you to shreds. As you are being torn apart, you think: 'I wish I had chosen a better door...' Better luck next time!"
            )
        elif choice3.lower() == "yellow":
            print(
                "You cautiously open the door, but nothing bad happens. You step through it and see the gigantic words: 'YOU WIN, CONGRATS' painted on a banner. Seems you have won some twisted game of luck. As you breathe a sign of relief, you start to wonder what is behind the other doors..."
            )
        else:
            print(
                "When you try to do anything other than choose a door to enter through, the floor falls out from beneath you, impaling you on spikes below. As you painfully breathe your last breath, you think: 'I wish I had chosen a door...' ... GAME OVER..."
            )
    else:
        print(
            "Oh no, you've made a bad choice and are now dead... better luck next time!"
        )

else:
    print(
        "Oh no, you've made a bad choice and are now dead... better luck next time!"
    )
