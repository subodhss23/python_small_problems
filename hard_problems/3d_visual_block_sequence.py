''' A block sequence in three dimensions. WE can write a formula for this one:

    one -> 5
    two -> 12
    three -> 20
    four -> 29
    five -> 39

    Create a function that takes a number(step) as an argument and returns the amount of blocks in that step. '''


def blocks(step):
    if step == 0:
        return 0
    sum = 5
    increase = 6
    for i in range(step - 1):
        increase += 1
        sum+= increase
    return sum


print(blocks(1))
print(blocks(5))
print(blocks(2))