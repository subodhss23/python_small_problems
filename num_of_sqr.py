''' Create a function that calculates the nubmer of different squares in an n * n square grid.'''

def number_squares(n):
    sum = 0 
    for i in range(n+1):
        sum += (i * i)
    return sum

print(number_squares(2))
print(number_squares(4))
print(number_squares(5))