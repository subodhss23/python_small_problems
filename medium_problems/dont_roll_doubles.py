''' John is playing a dice game. The rules are as follows.
    1. Roll two dice.
    2. Add the nubmers on the dice together.
    3. Add the total to your overall score.
    4. Repeat this for three rounds.

    But if you roll DOUBLES, your score is instantly wiped to 0 and your 
    game ends immediately!

    Create a function that takes in a list of tuples as input, and return
    John's score after this game has ended. '''

def dice_game(lst):
    total=0
    for a, b in lst:
        if a == b:
            return 0
        total+= a + b
    return total

print(dice_game([(1, 2), (3, 4), (5, 6)]))
print(dice_game([(1, 1), (5, 6), (6, 4)]))
print(dice_game([(4, 5), (4, 5), (4, 5)]))