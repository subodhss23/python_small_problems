''' What's the probability of someone making a certain amount of free throws in a row given their
    free throw success percentage? If Sally makes 50% of her free shot throws. Then Sally's probability
    of making 5 in a row would be 3%.'''

def free_throws(success, rows):
    new_str = success.strip('%')
    return str(round(round((int(new_str)/100) ** rows, 2) * 100)) + '%'


print(free_throws("75%", 5))
print(free_throws("25%", 3))
print(free_throws("90%", 30))