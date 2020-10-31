# find drinks without sugar
# which are cola and fanta

def skip_the_sugar(drinks):
    sugar_free = []
    sugar = ['cola', 'fanta']
    for i in drinks:
        if i not in sugar:
            sugar_free.append(i)
    return sugar_free

print(skip_the_sugar(['pepsi', 'cola']))
print(skip_the_sugar(["cola", "fanta"]))
print(skip_the_sugar(["cola", "fanta", "water"]))