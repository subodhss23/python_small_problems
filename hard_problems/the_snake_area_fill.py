''' This challenge is based on the classic videogame "Snake".

    Assume the game screen is an n * n square, and the snake starts the game with length 1 (i.e. just the head)
    positioned on the top left corner.

    for example, if n = 7 the game looks something like this:

    In this version of the game, the length of the snake dobules each time it eats food(e.g. if the length
    is 4, after eating it becomes 8).

    Create a function that takes the side n of the game screen and return the number of times the snake can
    eat before it runs out of space in the game screen.'''


def snakefill(n):
    result = 1
    count = 0
    while result*2 <= n**2:
        count+=1
        result*=2
        print(count)
        print(result)
    return count


print(snakefill(3))
# print(snakefill(6))
# print(snakefill(24))


# 3 - 3
# 6 - 5
# 24 - 9
# *4   +4