"""Simulates coffee machine.
"""

REPORT_KEYWORD = "report"

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 400,
    "milk": 400,
    "coffee": 200,
}


def check_resources(needed: dict, stock: dict = None):
    """Returns True if there is enough stock. Returns False otherwise.

    Args:
        needed (dict): Dict of ingredients required.
        stock (dict): Dict of ingredient-value pairs.
    """
    if stock is None:
        stock = {}

    is_enough = True
    for ingredient, amount in needed.items():
        if stock[ingredient] < amount:
            is_enough = False
            print(f"Not enough {ingredient}.")

    return is_enough


def transact(coffee_type: str, customer_money: float, menu: dict):
    """Returns change according to coffee type. Returns customer money if not
    enough for coffee of choice.

    Args:
        coffee_type (str): Type of coffee ordered.
        customer_money (float): Amount paid by customer.
        menu (dict): Dict of menu with costs.
    """

    cost = menu[coffee_type]["cost"]

    if customer_money < cost:
        print(f"Sorry, a {coffee_type} costs ${cost}. You only have ${customer_money}.")
        print(f"You have been refunded ${customer_money}")
        return customer_money

    change = customer_money - cost
    return change


def ask_money():
    """Prompts user for number of coins, and returns the sum."""
    MONEY_VALUE = {
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1,
    }

    total = 0
    for coin, value in MONEY_VALUE.items():
        total += value * int(input(f"Insert {coin}: "))

    return total / 100


def make_coffee(coffee_recipe: dict, stock: dict):
    """Makes coffee, and takes away the ingredients required from stock. Returns
    updated stock.

    Args:
        coffee_recipe (dict): Coffee ordered.
        stock (dict): Ingredients to take away from.
    """
    for ingredient, amount in coffee_recipe.items():
        stock[ingredient] -= amount

    return stock


def coffee_machine(coffee_menu: dict, ingredients_stock: dict, keyword: str):
    machine_state = True
    total_money = 0

    while machine_state:
        # Ask user for coffee
        coffee_choice = ""
        while coffee_choice not in coffee_menu:
            coffee_choice = input(
                "What would you like? (Espresso, Latte, Cappuccino): "
            ).lower()

            # Print out stock and total money collected.
            if coffee_choice == keyword:
                print(ingredients_stock)
                print(f"Total collected: ${total_money}")

            if coffee_choice == "off":
                machine_state = False
                break

        if coffee_choice == "off":
            print("Powering off . . .")
            break

        # Check inventory for coffee requirements.
        #   if not enough, warn user, end.
        #   if enough, continue
        if not check_resources(
            coffee_menu[coffee_choice]["ingredients"], ingredients_stock
        ):
            break

        # Let user pay by inserting coins
        #   if user money not enough, refund, end.
        #   if enough, return change and continue.
        user_money = ask_money()
        coffee_cost = coffee_menu[coffee_choice]["cost"]
        change = transact(coffee_choice, user_money, coffee_menu)
        if user_money < coffee_cost:
            break

        # "returns" change lol
        print(
            f"That would be ${coffee_cost}. Received ${user_money}. Here is ${change} in change."
        )
        total_money += coffee_cost

        # Make coffee
        coffee_ingredients = coffee_menu[coffee_choice]["ingredients"]
        ingredients_stock = make_coffee(coffee_ingredients, ingredients_stock)
        print(f"Here is your {coffee_choice}, enjoy friendo.")


coffee_machine(MENU, resources, REPORT_KEYWORD)
