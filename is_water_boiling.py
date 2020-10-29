''' create a function that determines if the temp of the water is considered
    boiling or not. temp will be measured in fahrenheit and celsius. '''


def is_boiling(temp):
    for i in temp:
        if i == 'F' or i == 'C':
            if temp >= '212F' or temp >= '100C':
                return True
            else:
                return False

print(is_boiling('212F'))
print(is_boiling('100C'))
print(is_boiling('0F'))