class MoneyMachine:
    """
    Handles money collection and payment processing for the coffee machine.
    """

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self, starting_money=0.0):
        """
        Initialize the machine with an optional starting amount of money.
        """
        self.money = starting_money

    def report(self):
        """
        Prints the current amount of money stored in the machine.
        """
        print(f"Money: ${self.money:.2f}")

    def collect_coins(self):
        """
        Prompts the user to insert coins and calculates the total value.

        Returns:
            float: Total value of coins inserted, rounded to 2 decimals.
        """
        print("Please insert coins.")
        total = 0.0
        for coin, value in self.COIN_VALUES.items():
            try:
                count = int(input(f"How many {coin}? "))
                total += count * value
            except ValueError:
                print(f"Invalid input for {coin}. Counting as 0.")
        return round(total, 2)

    def make_payment(self, drink_cost):
        """
        Processes the payment for a drink.

        Args:
            drink_cost (float): The cost of the selected drink.

        Returns:
            bool: True if payment is accepted, False otherwise.
        """
        received = self.collect_coins()
        if received < drink_cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False

        change = round(received - drink_cost, 2)
        if change > self.money:
            print("Sorry, I don't have enough change. Money refunded.")
            return False

        self.money += drink_cost
        if change > 0:
            print(f"Here is ${change} in change.")

        return True
