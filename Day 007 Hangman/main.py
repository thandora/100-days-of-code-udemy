# TODO- dont allow input >1 char
# 26/6/22
# Added display for incorrectly guessed letters.
# Lives no longer decrease when guessing already guessed letters.
# 25/6/22
# Fixed crash on guessing >1 char. 

import hangman_art
import hangman_words
import random

# Update the word list to use the 'word_list' from hangman_words.py
stages = hangman_art.stages
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
logo = hangman_art.logo
print(logo)

# Create blanks
display = []

# Store incorrect guessesr
incorrect_guesses = []
for _ in range(word_length):
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed:{guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess} is not in the word, try again.")
        if guess not in incorrect_guesses:
            incorrect_guesses.append(guess)
            lives -= 1
        if lives == 0:
            end_of_game = True
            print(f'You lose. The word was: "{chosen_word}"')

    print(f"{' '.join(display)}")

    # Display incorrectly played letters.
    print(f"Guessed: {incorrect_guesses}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])