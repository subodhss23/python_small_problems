#create a function that accepts a measurement value in inches and returns 
# the equivalent of the measurement value in feet.

def inches_to_feet(inches):
    if inches >= 12:
        return inches/12
    return 0


print(inches_to_feet(231))
print(inches_to_feet(12))
print(inches_to_feet(5))