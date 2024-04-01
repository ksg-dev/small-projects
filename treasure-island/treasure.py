explosion = r"""
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
          
"""

croc = r"""
   
                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-' .' /
                                    _____..'  .'
                                   '-._____.-'
"""
dog = r"""                          __
     ,                    ," e`--o
    ((                   (  | __,'
     \\~----------------' \_;/
hjw  (                      /
     /) ._______________.  )
    (( (               (( (
     ``-'               ``-'
     
"""

cage = r"""         __.-.__
     _.-'  ' `  `-._
   .'  '  '   `  `  `.
  ( '    '     `    ` )
  |`-,..,.____..,.,--;|
  |: |  :|  : | : |: ||
  |: |  :| (9>| : |: ||
  |: |  :|(\) | : |: ||
  |: |  :|/\\ | : |: ||
  |: |  /| II | : |: ||
  |: |///| II | : |: ||
  |; |  :| II | : |: ||
  /`-!...|____|...!--'\
 /                     \
 `--...._________....--'
 
"""

fireworks = r"""     .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
jgs     *
        *
"""

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

def get_direction():
    dir_choices = ['right', 'left']
    direction = input("You're at a crossroads. Where do you want to go? Type 'left' or 'right'\n").lower().strip()
    if direction not in dir_choices:
        return("Please type 'left' or 'right'")
    else:
        return(direction)

def get_mode():
    mode_choices = ['wait', 'swim']
    mode = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower().strip()
    if mode not in mode_choices:
        return("Please type 'wait' or 'swim'")
    else:
        return(mode)

def get_door():
    door_choices = ['red', 'blue', 'yellow']
    door = input("You arrive at the island unharmed. There is a house with 3 doors. Type 'red', 'blue', or 'yellow' to choose.\n").lower().strip()
    if door not in door_choices:
        return("Please type 'red', 'blue', or 'yellow'")
    else:
        return(door)

def choice():
    direction = get_direction()
    if direction == 'left':
        mode = get_mode()
        if mode == 'swim':
            print(croc)
            print("You were eaten trying to swim across. Game Over")
        elif mode == 'wait':
            door = get_door()
            if door == 'red':
                print(dog)
                print("There is a puppy behind the door. You are unable to stop petting him to continue. Game Over")
            elif door == 'blue':
                print(cage)
                print("You wandered into a trap and are now the beloved pet of a fairy. Game Over")
            elif door == 'yellow':
                print(fireworks)
                print("YOU WIN!!!")
            else:
                print(get_door)
        else:
            print(mode)
    elif direction == 'right':
        print(explosion)
        print("You wandered into a mine field and blew up. Game over")
    else:
        return(direction)


choice()
