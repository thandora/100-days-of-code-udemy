from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    menu2 = menu.get_items() # Redundant. Just for readability purpose.
    user_input = input(f"What would you like? ({menu2}): ").lower()

    if user_input == "off":
        machine_on = False
        print("Turning off. . .")

    elif user_input == "report":
        print("- - - - - - - - -")
        coffee_maker.report()
        print("- - - - - - - - -")
        money_machine.report()
        print("- - - - - - - - -")

    # Check if user input is in menu.
    elif not menu.find_drink(user_input) == None:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

