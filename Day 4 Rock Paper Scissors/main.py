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

# Write your code below this line 👇
choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
bot_choice = random.randint(0, 2)
print(choices[user_choice])
print(f"Computer chose:\n{choices[bot_choice]}")

# If user chooses rock.
if user_choice == 0:
    if bot_choice == 0:     # Bot chooses rock
        print("It's a tie!")
    elif bot_choice == 1:   # Bot chooses paper
        print("You lose!")
    elif bot_choice == 2:   # Bot chooses scissors
        print("You win!")


# User chooses paper.
elif user_choice == 1:
    if bot_choice == 0:     # Bot chooses rock
        print("You win!")
    elif bot_choice == 1:   # Bot chooses paper
        print("It's a tie!")
    elif bot_choice == 2:   # Bot chooses scissors
        print("You lose!")

# User chooses scissors.
elif user_choice == 2:
    if bot_choice == 0:     # Bot chooses rock
        print("You lose!")
    elif bot_choice == 1:   # Bot chooses paper
        print("You win!")
    elif bot_choice == 2:   # Bot chooses scissors
        print("It's a tie!")
