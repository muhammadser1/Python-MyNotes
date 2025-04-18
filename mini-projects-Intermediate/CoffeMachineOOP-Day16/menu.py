class MenuItem:
    """
    Represents a single item on the coffee machine menu.

    Attributes:
        name (str): The name of the drink (e.g., 'latte').
        cost (float): The price of the drink.
        ingredients (dict): A dictionary containing ingredient amounts (water, milk, coffee).
    """
    def __init__(self, name, cost, water, milk, coffee):
        """
        Initializes a MenuItem with its name, cost, and ingredient requirements.

        Args:
            name (str): Name of the drink.
            cost (float): Price of the drink.
            water (int): Amount of water needed in ml.
            milk (int): Amount of milk needed in ml.
            coffee (int): Amount of coffee needed in grams.
        """
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """
    Represents the coffee machine's entire menu containing multiple MenuItems.
    """
    def __init__(self):
        """
        Initializes an empty menu.
        """
        self.menu = []

    def add_menu_item(self, menu_item):
        """
        Adds a new MenuItem to the menu.

        Args:
            menu_item (MenuItem): The drink item to add to the menu.
        """
        self.menu.append(menu_item)

    def get_items(self):
        """
        Returns a list of names of all drinks currently in the menu.

        Returns:
            list[str]: The drink names.
        """
        return [item.name for item in self.menu]

    def find_item(self, item_name):
        """
        Searches for a MenuItem by its name.

        Args:
            item_name (str): The name of the drink to find.

        Returns:
            MenuItem or None: The matching MenuItem object, or None if not found.
        """
        for item in self.menu:
            if item.name == item_name:
                return item
        return None
