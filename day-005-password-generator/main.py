#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',\
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_length = nr_letters + nr_symbols + nr_numbers 

#Create a list for chars of password.
#Also create a list for position of characters.
password = []
position = []
for x in range(0, password_length):
  password.append("")
  position.append(x)

#Create password
for x in range(0, password_length):

  #Choose random position in current pool.
  cr_position = random.choice(position)
  #Remove randomly selected position from position list.
  position.remove(cr_position)

  #Place random character in current position (cr_position).
  if nr_letters:    #Exhaust letters first.
    password[cr_position] = random.choice(letters)
    nr_letters -= 1
  elif nr_symbols:  #Exhaust symbols.
    password[cr_position] = random.choice(symbols)
    nr_symbols -= 1
  elif nr_numbers:  #Exhaust numbers.
    password[cr_position] = random.choice(numbers)
    nr_numbers -= 1

#Convert list of characters to string
password = ''.join(password)
print(f"\n\n{password}\n\n")