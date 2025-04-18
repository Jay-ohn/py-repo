import random
import time

Choice = input("Heads or Tails? H/T: ").upper()
User_choice = "HEADS" if Choice == "H" else "TAILS" \
    if Choice == "T" else None

print("\nYou chose: " + User_choice if User_choice is not None
      else "\nInvalid Choice!")

probability = random.randint(0, 1)
if probability == 0:
    Computer_choice = "HEADS"
else:
    Computer_choice = "TAILS"

print("Computer chose: " + Computer_choice + "\n")

if User_choice is None:
    print("You Lose!\nChoose either H or T next time!")
elif User_choice == Computer_choice:
    print("You win!")
else:
    print("You lose!")

time.sleep(3)
exit()
