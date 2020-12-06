''' Build a function that creates histogram. Every bar needs to be on a new line 
    and its length corresponds to the number in the list passes as an arguement.
    The second argument of the function represents the character that needs to
    be used.'''


def histogram(lst, char):
    new_lst = []
    for i in lst:
        new_lst.append(i*char)
    return ('\n').join(new_lst)

print(histogram([1, 3, 4], "#"))
print(histogram([6, 2, 15, 3], "=") )
print(histogram([1, 10], "+"))