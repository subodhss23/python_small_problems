''' "Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one
    by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves
    them back.

    Given a number of petals, return a string which repeats the phrases "Loves me" and "loves me not" for
    every alternating petal, and return the last phrase in all caps. Remember to put a comma and space 
    between phrases. '''

def loves_me(n):
    last_one = "LOVES ME"
    new_lst = []
    for i in range(1, n+1):
        if i % 2 != 0:
            new_lst.append('Loves me')
        elif i % 2 == 0:
            new_lst.append("Loves me not")
    new_lst = new_lst[:-1] + [new_lst[-1].upper()]
    return (', ').join(new_lst)


print(loves_me(3))
print(loves_me(6))
print(loves_me(1))