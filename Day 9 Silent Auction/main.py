# from replit import clear   # For replit only
from art import logo
# HINT: You can call clear() to clear the output in the console.
print(logo)
print("<<WELCOME SCREEN>>")
is_running = True
bidders = {}

while is_running:
    bidder_name = input("Who u m8: ")
    bidder_bid = float(input("How much u bid m8: "))

    bidders[bidder_name] = bidder_bid

    choice_continue = None
    while choice_continue not in ["y", "n"]: 
        choice_continue = input("other bidder? y/n: ").lower()
        # clear() # For replit only
    if choice_continue == "n":
        is_running = False

highest_bid = 0
highest_bidder = ""
for name in bidders:
    if bidders[name] > highest_bid:
        highest_bidder = name
        highest_bid = bidders[name]
        
print(f"{highest_bidder} wins with a bid of {highest_bid}.")