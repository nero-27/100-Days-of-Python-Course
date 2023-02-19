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
    }
}

stock = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(resources):
    for key, value in resources.items():
        print(f"{key}: {value}")


def is_resources_enough(coffee_ingredients):
    for item in coffee_ingredients:
        if coffee_ingredients[item] > stock[item]:
            print(f"Sorry. Not enough {item}")
            return False
    return True


def calculate_change(coffee_price, user_paid):
    return user_paid-coffee_price


def is_transaction_successful(coffee_price, user_paid):
    if user_paid > coffee_price or user_paid == coffee_price:
        return True
    return False


def make_coffee(ingredients, resources):
    for item in resources:
        if item in ingredients:
            resources[item] -= ingredients[item]


def insert_coins():
    print("Please insert coins.")
    q = int(input("How many quarters? ")) * 0.25
    d = int(input("How many dimes? ")) * 0.10
    n = int(input("How many nickels? ")) * 0.05
    p = int(input("How many pennies? ")) * 0.01
    total = q + d + n + p
    return total


while True:
    drink = input("What would you like? (Espresso / Latte / Cappuccino) : ").lower()
    if drink == 'off':
        print("Shutting down...")
        break
    if drink == 'report':
        print_report(stock)
        break

    coffee = MENU[drink]

    coffee_price = coffee["cost"]
    if is_resources_enough(coffee["ingredients"]):
        user_paid = insert_coins()
        if is_transaction_successful(coffee_price, user_paid):
            make_coffee(coffee["ingredients"], stock)
            if user_paid > coffee_price:
                change = calculate_change(coffee_price, user_paid)
                print(f"Here's your change: {change}")
                print(f"Enjoy your coffee!!")
            else:
                print(f"No change. You paid perfect amount.")
                print(f"Enjoy your coffee!!")
        else:
            print("Sorry. You did not pay enough.")

    else:
        continue







