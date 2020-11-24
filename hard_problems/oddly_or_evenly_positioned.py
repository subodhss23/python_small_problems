'''Create a function that returns the characters from a list or string r on odd or even positions, depending on the specifier
    s. The specifier will be "odd" for items on odd positions(1,3,5,....) and "even" for items on even positions(2,4,6,...)'''


def char_at_pos(r, s):
    if type(r) == list:
        new_lst = []
        if s == 'even':
            for i in range(len(r)):
                if i % 2 != 0:
                    new_lst.append(r[i])
        elif s == 'odd':
            for i in range(len(r)):
                if i % 2 == 0:
                    new_lst.append(r[i])
        return new_lst
    elif type(r) == str:
        new_str = ""
        if s == 'even':
            for i in range(len(r)):
                if i % 2 != 0:
                    new_str+=r[i]
        elif s == 'odd':
            for i in range(len(r)):
                if i % 2 == 0:
                    new_str+=r[i]
        return new_str


print(char_at_pos([2, 4, 6, 8, 10], "even"))
print(char_at_pos("EDABIT", "odd"))
print(char_at_pos(["A", "R", "B", "I", "T","R", "A", "R", "I", "L", "Y"], "odd"))
