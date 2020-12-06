''' Create a function that takes a list of dictionaries(groceries) which calcualtes the total price and returns it
    as a number. A grocery dictionary has a product, a quantity and a price, for example:

        {
            "product": "Milk",
            "quantity": 1,
            "price": 1.50
        }
'''

def get_total_price(groceries):
    sum = 0
    for i in range(len(groceries)):
        sum+= groceries[i]["quantity"] * groceries[i]["price"]
    return round(sum, 1)

print(get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 }
]))

print(get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Cereals", "quantity": 1, "price": 2.50 }
]))

print(get_total_price([
  { "product": "Milk", "quantity": 3, "price": 1.50 }
]))

print(get_total_price([
	{ "product": "Milk", "quantity": 1, "price": 1.50 },
	{ "product": "Cereals", "quantity": 1, "price": 2.50 }
]))