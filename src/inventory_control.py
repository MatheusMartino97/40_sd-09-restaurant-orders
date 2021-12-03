class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }
        self.orders = []

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if (self.inventory[ingredient] - 1 < 0) or (not self.inventory):
                return False

            self.inventory[ingredient] -= 1
            self.orders.append((customer, order, day))

    def get_quantities_to_buy(self):
        quantities_to_buy = {}

        for ingredient in self.inventory:
            quantity_to_buy = (
                self.MINIMUM_INVENTORY[ingredient] - self.inventory[ingredient]
            )

            if quantity_to_buy >= 0:
                quantities_to_buy[ingredient] = quantity_to_buy

        return quantities_to_buy

    def get_available_dishes(self):
        available_dishes = set()

        for (dish, ingredients) in self.INGREDIENTS.items():
            is_dish_available = True
            
            for ingredient in ingredients:
                if is_dish_available == True:
                    if self.inventory[ingredient] == 0:
                        print(ingredient, 'zerou')
                        is_dish_available = False

            if is_dish_available == True:
                available_dishes.add(dish)

        return available_dishes
