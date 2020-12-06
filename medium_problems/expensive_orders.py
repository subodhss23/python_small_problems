''' Write a function taht has two parameters: orders and cost. Return any orders that are greater
    than the cost. '''

def expensive_orders(orders, cost):
    new_obj = {}
    for key, value in orders.items():
        if value > cost:
            new_obj[key] = value
    return new_obj

print(expensive_orders({ "a": 3000, "b": 200, "c": 1050 }, 1000))
print(expensive_orders({ "Gucci Fur": 24600, "Teak Dining Table": 3200, "Louis Vutton Bag": 5550, "Dolce Gabana Heels": 4000 }, 20000))
print(expensive_orders({ "Deluxe Burger": 35, "Icecream Shake": 4, "Fries": 5 }, 40))