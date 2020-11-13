''' Using list comprehensions, create a function that finds all even nubmers
    from 1 to the given nubmer.'''

# def find_even_nums(n):
#     new_arr = []
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             new_arr.append(i)
#     return new_arr

# def find_even_nums(n):
#     new_arr = []
#     i = 1
#     while(i<= n):
#         if i % 2 == 0:
#             new_arr.append(i)
#         i+=1
#     return new_arr

def find_even_nums(num):
    return [i for i in range(2,num+1, 2)]

print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(2))