import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''




def main():
    play = [rock, paper, scissors]
    
    player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
    computer = random.randint(0,2)
    options = [0, 1, 2]

    if player not in options:
        print("You typed an invalid number, you lose!")
    else:

        
        player_pic = play[player]
       
        comp_pic = play[computer]

        if player == 0 and computer == 2:
            print(f"You chose: \n{player_pic}")
            print(f"Computer Chose:\n{comp_pic}")
            print("You win!")
        elif player == 2 and computer == 0:
            print(f"You chose: \n{player_pic}")
            print(f"Computer Chose:\n{comp_pic}")
            print("You Lose!")
        elif player < computer:
            print(f"You chose: \n{player_pic}")
            print(f"Computer Chose:\n{comp_pic}")
            print("You lose")
        elif player > computer:
            print(f"You chose: \n{player_pic}")
            print(f"Computer Chose:\n{comp_pic}")
            print("You win!")
        elif player == computer:
            print(f"You chose: \n{player_pic}")
            print(f"Computer Chose:\n{comp_pic}")
            print("It's a draw")
       

main()