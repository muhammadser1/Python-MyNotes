class CoffeeMachineApp:
    def __init__(self, menu, coffee_maker, money_machine):
        self.menu = menu
        self.coffee_maker = coffee_maker
        self.money_machine = money_machine
        self.is_on = True

    def run(self):
        while self.is_on:
            options = "/".join(self.menu.get_items())
            choice = input(f"What would you like? ({options}): ").lower()

            if choice == "off":
                print("Shutting down...")
                self.is_on = False
            elif choice == "report":
                self.coffee_maker.report()
                self.money_machine.report()
            else:
                drink = self.menu.find_item(choice)
                if drink and self.coffee_maker.is_resource_sufficient(drink):
                    if self.money_machine.make_payment(drink.cost):
                        self.coffee_maker.make_coffee(drink)
