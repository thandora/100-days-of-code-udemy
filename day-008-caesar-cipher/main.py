"""
Caesar cipher. Where input string is shifted n times according to the user.
Outputs encoded/ decoded string.
"""

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


# Caesar function
def caesar(text, shift, code_type):
    caesar_text = ""
    text_type = "encoded"  # For print format purpose.

    # Ensure user input is within range.
    # This is only useful for decoding, encoding has it's fail-safe built-in.
    if shift > 26:
        shift %= 26

    # Change direction of shift in case of decoding.
    if code_type == "decode":
        shift *= -1
        text_type = "decoded"

    # Take each character in string and shift it if it's in the alphabet, otherwrise don't change it.
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)  # Current index to be shifted
            shifted_index = position + shift  # Shift index by "shift" amount of times.
            if shifted_index > 25:  # Loop back to "A" if shifted index exceeds "Z"
                shifted_index = (shifted_index % 25) - 1

            # Hold en/decoded character.
            new_letter = alphabet[shifted_index]
        else:
            new_letter = letter

        # Add shifted character to en/decoded string.
        caesar_text += new_letter

    # Print en/decoded string.
    print(f"\nThe {text_type} text is:\n{caesar_text}\n")


will_continue = True
continue_choice = ""
direction = ""

# Control loop if user wants to restart.
while will_continue:

    # Ensure user input is of expected value.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction not in ["encode", "decode"]:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # String to be en/decoded. Entered by user.
    text = input("Type your message:\n").lower()

    # Ensure user input is of expected value.
    shift = None
    while shift is None:
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Enter a valid number.")

    # Ensure user input is of expected value.
    while not isinstance(shift, int):
        shift = int(input("Type the shift number:\n"))

    # Run caesar cipher
    caesar(text, shift, direction)

    # Ensure user input is of expected value.
    continue_choice = input("Do you want to start again? y / n\n").lower()
    while continue_choice not in ["y", "n"]:
        continue_choice = input("Do you want to start again? y / n\n").lower()

    # Exit loop if user chooses "n".
    if continue_choice == "n":
        will_continue = False
        print("Goodbye.")
