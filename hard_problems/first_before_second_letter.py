''' You are given three input: a string, one leter, and a second letter.

    Write a function that returns True if every instance of the first letter 
    occurs before every instance of the second letter. '''


def first_before_second(s, first, second):
    first_found = False
    second_found = False
    for letter in s:
        if letter == first:
            if second_found:
                return False
            first_found = True
        elif letter == second:
            if first_found == False:
                return False
            second_found = True
    return True

print(first_before_second("a rabbit jumps joyfully", "a", "j") )
print(first_before_second("knaves knew about waterfalls", "k", "w") )
print(first_before_second("happy birthday", "a", "y") )
print(first_before_second("precarious kangaroos", "k", "a"))