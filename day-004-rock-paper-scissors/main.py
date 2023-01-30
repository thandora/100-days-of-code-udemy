import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]
game_running = True
score = {"wins": 0, "loses": 0, "draws": 0}

while game_running:
    user_choice = input(
        'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "x" to end\n'
    ).lower()
    if user_choice == "x":
        game_running = False
        break

    user_choice = int(user_choice)

    bot_choice = random.randint(0, 2)
    print(choices[user_choice])
    print(f"Computer chose:\n{choices[bot_choice]}")

    # If user chooses rock.
    if user_choice == 0:
        if bot_choice == 0:  # Bot chooses rock
            print("It's a tie!")
            score["draws"] += 1
        elif bot_choice == 1:  # Bot chooses paper
            print("You lose!")
            score["loses"] += 1
        elif bot_choice == 2:  # Bot chooses scissors
            print("You win!")
            score["wins"] += 1

    # User chooses paper.
    elif user_choice == 1:
        if bot_choice == 0:  # Bot chooses rock
            print("You win!")
            score["wins"] += 1
        elif bot_choice == 1:  # Bot chooses paper
            print("It's a tie!")
            score["draws"] += 1
        elif bot_choice == 2:  # Bot chooses scissors
            print("You lose!")
            score["loses"] += 1

    # User chooses scissors.
    elif user_choice == 2:
        if bot_choice == 0:  # Bot chooses rock
            print("You lose!")
            score["loses"] += 1
        elif bot_choice == 1:  # Bot chooses paper
            print("You win!")
            score["wins"] += 1
        elif bot_choice == 2:  # Bot chooses scissors
            print("It's a tie!")
            score["draws"] += 1

    score_sum = 0
    for _ in score.values():
        score_sum += _

    winrate = score["wins"] / (score_sum)

    print(
        f"""Wins: {score["wins"]}
Loses: {score["loses"]}
Draws: {score["draws"]}
win rate:{winrate * 100:.2f}%"""
    )
    print("-" * 30)
