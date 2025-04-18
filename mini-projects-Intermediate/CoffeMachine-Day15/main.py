from MENU import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def prompt_user():
    """Prompt the user to choose a drink or enter a command."""
    valid_choices = list(MENU.keys()) + ["report", "off"]
    prompt = f"What would you like? ({'/'.join(MENU.keys())}): "

    while True:
        user_input = input(prompt).lower().strip()

        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid input. Please choose from espresso, latte, cappuccino, report, or off.")


def print_report():
    """Prints the current status of machine resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def is_resource_sufficient(drink_name):
    """Returns True if resources are sufficient to make the drink, else False with all missing items."""
    ingredients = MENU[drink_name]['ingredients']
    missing = False

    for item, required in ingredients.items():
        if required > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            missing = True
    return not missing


def collect_coins():
    """Prompts the user to insert coins and returns the total amount as a float."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ($0.25): "))
    dimes = int(input("How many dimes? ($0.10): "))
    nickels = int(input("How many nickels? ($0.05): "))
    pennies = int(input("How many pennies? ($0.01): "))

    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return round(total, 2)


def is_transaction_successful(payment, drink_cost):
    """Returns True if payment is sufficient, adds profit, and returns change if needed."""
    if payment < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False

    change = round(payment - drink_cost, 2)
    if change > 0:
        print(f"Here is ${change} in change.")

    resources["money"] += drink_cost
    return True


def make_coffee(drink_name):
    """Deducts the ingredients from resources and serves the drink."""
    ingredients = MENU[drink_name]['ingredients']
    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {drink_name}. Enjoy!")


def start_coffee_machine():
    """Main loop to run the coffee machine and serve customers."""
    is_on = True

    while is_on:
        choice = prompt_user()

        if choice == "off":
            print("Turning off the coffee machine. Goodbye! 👋")
            is_on = False

        elif choice == "report":
            print_report()

        else:
            drink = MENU[choice]
            if is_resource_sufficient(choice):
                payment = collect_coins()
                if is_transaction_successful(payment, drink['cost']):
                    make_coffee(choice)


start_coffee_machine()