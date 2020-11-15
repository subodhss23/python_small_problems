'''Create a function that returns the list of numbers from a given range. But for
    multiples of three, return "Eda" instread of the number and for the multiples
    of five, return "Bit". For nubmers which are multiples of both three and five, 
    return "Edabit".'''


def eda_bit(start, end):
    new_lst = []
    for i in range(start, end+1):
        if i % 3 == 0 and i % 5 == 0 or i == 0:
            new_lst.append('EdaBit')
        elif i % 3 == 0:
            new_lst.append('Eda')
        elif i % 5 == 0:
            new_lst.append('Bit')
        else:
            new_lst.append(i)
    return new_lst

print(eda_bit(0, 10))
print(eda_bit(14, 20))
print(eda_bit(99, 106))