''' Create a function that accepts a list of two stings and checks if the letters in the second
    string are present in the first string. '''


def letter_check(lst):
    payload = lst[1].lower()
    target = lst[0].lower()
    for i in payload:
        if i not in target:
            return False
    return True

print(letter_check(["trances", "nectar"]))
print(letter_check(["compadres", "DRAPES"]))
print(letter_check(["parses", "parsecs"]) )