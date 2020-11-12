''' A typical car can hold four passengers and one driver, allowing five people
    to travel around. Given n number of people, return how many cars are needed
    to seat everyone comfortably. '''
import math
def cars_needed(n):
    return math.ceil(n / 5)

print(cars_needed(5))
print(cars_needed(11))
print(cars_needed(0))
print(cars_needed(2))
print(cars_needed(6))