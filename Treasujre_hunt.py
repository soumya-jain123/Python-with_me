print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 



first_choice = input('You are on a crossroad, where do you want to go? Left or right\n').lower()


if first_choice == 'left':
  second_choice = input('You have come to a lake. There is an island in the middle of the lake. Do you wait or swim?\n"').lower()


  if second_choice == 'wait':

    third_choice = input('You have arrived the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n').lower()


    if third_choice == 'blue':
      print('Eaten by beasts. Game over')
    elif third_choice == 'red':
      print('burned by fire. Game over')
    elif third_choice == 'yellow':
      print('Congratulation! you have sucessfully found the treasure')
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
    else:
      print('Game over.')


  else:
    print('swallowed by a shark. Game over')

else:
  print('oops! wrong choice. Game over')
