# Choose difficulty (Easy, hard, or custom)
# Guess a number
# Warn user if too high or too low
from random import randint
from art import logo

LIVES_HARD = 6
LIVES_EASY = 12

# Random number will be between these two numbers, inclusive.
LOWER_BOUND = 1
UPPER_BOUND = 2111


def guess_number(guess: int, lives: int, answer: int):
    """Compares <guess> against <answer>, and returns <lives> accordingly."""
    if guess != answer:
        lives -= 1

        if guess > answer:
            print("Too high!")
        else:
            print("Too low!")

    else:
        print("You won!")

    return lives


def difficulty_set():
    """Sets lives according to difficulty

    Returns:
        int: amount of lives
    """
    level = input("Choose a difficulty. E: easy, H: hard, C: custom: ").lower()
    if level == "e":
        lives = LIVES_EASY
    elif level == "h":
        lives = LIVES_HARD
    else:
        lives = int(input(("Enter number of lives you want: ")))

    return lives


def game():
    """Game loop

    Returns:
        int: returns 1 if game won, else 0.
    """
    print(logo)
    print(f"Hmm, I'm thinkin of a number between {LOWER_BOUND} and {UPPER_BOUND}.")
    lives = difficulty_set()
    answer = randint(LOWER_BOUND, UPPER_BOUND)
    guess = None
    while lives:
        guess = int(input("Guess the number: "))
        lives = guess_number(guess, lives, answer)

        if guess == answer:
            return 1

        if guess != answer:
            print(f"Lives: {lives}\n")

        if lives == 0:
            print(f"Game over. The number is {answer}.")
            return 0


game()
