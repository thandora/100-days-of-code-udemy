path_letter = r"Input/Letters/starting_letter.txt"
path_names = r"Input/Names/invited_names.txt"
path_output = r"Output/ReadyToSend/"
# with open(path_letter, "r") as f:
#     print(f.readline())

with open(path_letter, "r") as f:
    letter = f.read()

    with open(path_names, "r") as f:
        invited_names = f.readlines()
        print(invited_names)

        for name in invited_names:
            name = name.strip()
            letter.replace("[name]", name)
            new_path_output = path_output + f"letter_for_{name}.txt"

            with open(new_path_output, "w") as f:
                f.write(letter)
