from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create objects of all three classes
coffee_menu = Menu()
maker = CoffeeMaker()
machine = MoneyMachine()

# ask user for coffee
while True:
    user_input = input(f"Which coffee would you like? {coffee_menu.get_items()}")
    if user_input == 'report':
        maker.report()
        machine.report()
        break

    if user_input == 'off':
        print("Shutting down...")
        break

    # find_drink from menu
    coffee = coffee_menu.find_drink(user_input)

    # check resource sufficient
    if coffee:
        if maker.is_resource_sufficient(coffee):
            # process coins from money_machine
            if machine.make_payment(coffee.cost):
                # make coffee
                maker.make_coffee(coffee)

    more_coffee = input("Would you like another coffee? (y/n)? :")
    if more_coffee == 'n':
        break