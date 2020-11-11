''' Create a function that takes date in the format yyyy/mm/dd as an input and returns
    "Bonfire toffee" if the date is Octover 31, else return "toffee".'''

def halloween(dt):
    new_date = dt.split('/')
    if new_date[1] == '10' and new_date[2] == '31':
        return 'Bonfire toffee'
    else:
        return 'toffee'

print(halloween("2013/10/31"))
print(halloween("2012/07/31"))
print(halloween("2011/10/12"))