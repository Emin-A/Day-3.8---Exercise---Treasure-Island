# Treasure Island Game !
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
path_one = "left"
path_two = "swim"
path_three = "red"

print("Welcome to Treasure Island!")
print("Your mission is to find the hidden treasure!")
path_one = input("You are stranded on an island and in front of you there two paths, left and right.\nWhich path do you choose?\n")
if path_one == "right":
  print("You fell into a pit of snakes, scorpions and crocodiles!\nGAME OVER!")
elif path_one == "left":
  path_two = input("There is pond in your way, do you choose to swim or wait?\n")
  if path_two == "wait":
    print("A bunch of cannibals attack you from the bushes and they brutally murder you!\nGAME OVER!")
  elif path_two == "swim":
    path_three = input("You have arrived at a abandoned castle but there are three entrance doors.\nWhich door do you enter, the red one, green one, or the yellow one?\n")
    if path_three == "yellow":
      print("You wake up from a dream!\nTHE END!...or is it?")
    elif path_three == "green":
      print("You enter the room and there is a portal to another world floating in the air. \nYou jump through the portal but land on Teletubbies Island...\nGAME OVER!")
    elif path_three == "red":
      print("You enter a safe haven room full of treasure and food and you live like a KING!\nHail to the king baby!\nTHE END")
  
else:
  print("GAME OVER!")


# path_three = "swim"
# path_four = "wait"
# red_door = "red"
# green_door = "green"

# if input() == path_one:
#   print("There is pond in your way, do you choose to swim or wait?/n")
#   input()
#   if input() == path_three:
#     input(print("You have arrived at a abandoned castle but there two entrance doors./n Which door do you enter, the red one or the green one?/n"))
#     if input() == red_door:
#       input(print("You enter a safe haven room full of treasure and food and you live like a KING!/nHail to the king baby!/nTHE END"))
#     elif input() == green_door:
#       print("You enter the room and there is a portal to another world floating in the air. /nYou jump through the portal but land on Teletubbies Island.../nGAME OVER!")
#   elif input() == path_four:
#     print("A bunch of cannibals attack you from the bushes and they brutally murder you!/nGAME OVER!")
# elif input() == path_two:
#   print("You fell into a pit of snakes, scorpions and crocodiles!/nGAME OVER!")