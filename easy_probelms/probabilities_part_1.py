''' Given a list of numbers and a value n, write a function that returns the
    probabilit of choosing a number greater than or equal to n from the list.
    The probability should be express as a percentage, rounded to the one decimal place.'''


def probability(lst, n):
    new_lst = []
    for i in lst:
        if i >= n:
            new_lst.append(i)
    return round(100 * len(new_lst) / len(lst), 1)

print(probability([5, 1, 8, 9], 6))
print(probability([7, 4, 17, 14, 12, 3], 16))
print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))
