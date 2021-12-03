from src.analyze_log import (
    get_days_off_by_client,
    get_most_ordered_by_client,
    get_never_ordered_by_client
)


class TrackOrders:
    def __init__(self):
        self.orders = []
        self.days = {}

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))

        if day not in self.days:
            self.days[day] = 1
        else:
            self.days[day] += 1

    def get_most_ordered_dish_per_costumer(self, customer):
        return get_most_ordered_by_client(customer, self.orders)

    def get_never_ordered_per_costumer(self, customer):
        return get_never_ordered_by_client(customer, self.orders)

    def get_days_never_visited_per_costumer(self, customer):
        return get_days_off_by_client(customer, self.orders)

    def get_busiest_day(self):
        day_index = 0
        quantity_index = 1

        def extractor(day_quantity):
            return day_quantity[quantity_index]

        return max(self.days.items(), key=extractor)[day_index]

    def get_least_busy_day(self):
        day_index = 0
        quantity_index = 1

        def extractor(day_quantity):
            return day_quantity[quantity_index]

        return min(self.days.items(), key=extractor)[day_index]
