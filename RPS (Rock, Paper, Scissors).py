import random
import time

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

computer_choice = random.randint(0, 2)
user_choice = int(input("Alright! let's settle this once and for all.\n"
                     "Rock, Paper, Scissors! What do you choose? "
                     "\n\nType 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice not in [0, 1, 2]:
    print("\nInvalid choice! Please restart the game and choose a valid option.")
    time.sleep(3)
    exit()

print("\nYou chose: ", rock if user_choice == 0 else paper if user_choice == 1 else scissors)

print("Computer chose: ", rock if computer_choice == 0 else paper if computer_choice == 1 else scissors)

print("You win!" if (user_choice == 0 and computer_choice == 2) or
                    (user_choice == 1 and computer_choice == 0) or
                    (user_choice == 2 and computer_choice == 1) else
      "It's a draw!" if user_choice == computer_choice else
      "You lose! Go home and practice more!")

time.sleep(3) 
exit()
