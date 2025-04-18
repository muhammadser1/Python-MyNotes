from coffee_machine_app import CoffeeMachineApp
from menu import Menu,MenuItem
from coffemaker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    menu = Menu()
    menu.add_menu_item(MenuItem("espresso", 1.5, 50, 0, 18))
    menu.add_menu_item(MenuItem("latte", 2.5, 200, 150, 24))
    menu.add_menu_item(MenuItem("cappuccino", 3.0, 250, 100, 24))

    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    app = CoffeeMachineApp(menu, coffee_maker, money_machine)
    app.run()
