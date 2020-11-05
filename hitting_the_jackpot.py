''' create a function that takes a list(slot machine outcome) and returns True if all elements
    in the list are identical, and False otherwise. The list will contain 4 elements.'''

def test_jackpot(lst):
    return len(set(lst)) == 1

print(test_jackpot(["@", "@", "@", "@"]))
print(test_jackpot(["abc", "abc", "abc", "abc"]))
print(test_jackpot(["SS", "SS", "SS", "SS"]))
print(test_jackpot(["&&", "&", "&&&", "&&&&"]))
print(test_jackpot(["SS", "SS", "SS", "Ss"]))