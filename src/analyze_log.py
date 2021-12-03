import csv


def read_file_into_list(path_to_file):
    orders = []
    with open(path_to_file) as file:
        reader = csv.reader(file)
        for line in reader:
            orders.append(line)
    return orders


def get_most_ordered_by_client(client, orders):
    orders_by_product = {}

    for order in orders:
        name_index = 0
        product_index = 1
        name = order[name_index]
        product = order[product_index]

        if name == client:
            if product not in orders_by_product:
                orders_by_product[product] = 1
            else:
                orders_by_product[product] += 1

    def extractor(product_quantity):
        return product_quantity[product_index]

    return max(orders_by_product.items(), key=extractor)[name_index]


def get_times_ordered_by_client(client, ordered_product, orders):
    times_ordered_by_client = 0

    for order in orders:
        name = order[0]
        product = order[1]

        if name == client and ordered_product == product:
            times_ordered_by_client += 1

    return times_ordered_by_client


def get_never_ordered_by_client(client, orders):
    name_index = 0
    product_index = 1
    products_set = set([order[product_index] for order in orders])
    ordered_by_client = []
    never_ordered = []

    for order in orders:
        name = order[name_index]
        product = order[product_index]

        if name == client and product not in ordered_by_client:
            ordered_by_client.append(product)

    for each_product in products_set:
        if each_product not in ordered_by_client:
            never_ordered.append(each_product)

    never_ordered_set = set(never_ordered)
    return never_ordered_set


def get_days_off_by_client(client, orders):
    name_index = 0
    day_index = 2
    days_set = set([order[day_index] for order in orders])
    visited_days_by_client = []
    days_off = []

    for order in orders:
        name = order[name_index]
        product = order[day_index]

        if name == client and product not in visited_days_by_client:
            visited_days_by_client.append(product)

    for each_product in days_set:
        if each_product not in visited_days_by_client:
            days_off.append(each_product)

    days_off_set = set(days_off)
    return days_off_set


def analyze_log(path_to_file):
    orders = read_file_into_list(path_to_file)

    most_ordered_by_client = get_most_ordered_by_client('maria', orders)
    never_ordered_by_client = get_never_ordered_by_client('joao', orders)
    days_off_by_client = get_days_off_by_client('joao', orders)
    times_ordered_by_client = get_times_ordered_by_client(
        'arnaldo',
        'hamburguer',
        orders
    )

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.writelines(
            f"{most_ordered_by_client}\n"
            f"{times_ordered_by_client}\n"
            f"{never_ordered_by_client}\n"
            f"{days_off_by_client}\n"
        )
