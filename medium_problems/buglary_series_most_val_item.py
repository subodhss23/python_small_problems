''' You call your spouse to inform his/her most percious item is gone! Given a dictionary of stolen items,
    return the most expensive item on the items.'''

def most_expensive_item(products):
    max_item = max(list(products.values()))
    for item, price in products.items():
        if max_item == price:
            return item

print(most_expensive_item({
  "piano": 2000,
}))

print(most_expensive_item({
  "tv": 30,
  "skate": 20,
}))

print(most_expensive_item({
  "tv": 30,
  "skate": 20,
  "stereo": 50,
}))