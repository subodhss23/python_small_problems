''' In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that 
    each number is the sum of two preceding ones, starting from 0 and 1:

    Fibonacci Sequence
    and

    Fibonacci Sequence 2

    for n > 1

    The beginning of the sequence is thus:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

    The function fastFib(num) returns the fibonacci number Fn, of the given num as an arguement.'''


# def fib_fast(num):
#     a, b = 0, 1
#     for _ in range(num - 1):
#         a , b = b, a + b
#     return b

def fib_fast(num):
    lst = [0, 1]
    while len(lst)<=num:
        lst.append(lst[-2] + lst[-1])
    return lst[num]

print(fib_fast(5))
print(fib_fast(10))
print(fib_fast(20))
print(fib_fast(50))