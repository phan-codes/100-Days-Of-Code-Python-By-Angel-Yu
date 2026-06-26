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
player_choice_digit = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))


outcomes = [rock, paper, scissors]
computer_choice_digit = random.randint(0, len(outcomes) - 1)

player_choice = outcomes[player_choice_digit]
computer_choice = outcomes[computer_choice_digit]

win_message = "You win!!!"
lose_message = "You lose!!!"

print(f"You chose: \n{player_choice} \nComputer chose: \n{computer_choice}")

if computer_choice_digit == player_choice_digit: 
    print("Nobody wins!")  
elif computer_choice_digit == 0 and player_choice_digit == 1:
    print(win_message)
elif computer_choice_digit == 0 and player_choice_digit == 2: 
    print(lose_message)
elif computer_choice_digit == 1 and player_choice_digit == 0:
    print(lose_message)
elif computer_choice_digit == 1 and player_choice_digit == 2:
    print(win_message)
elif computer_choice_digit == 2 and player_choice_digit == 0:
    print(win_message)
elif computer_choice_digit == 2 and player_choice_digit == 1:
    print(lose_message)