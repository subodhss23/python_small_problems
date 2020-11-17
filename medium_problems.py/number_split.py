''' Given a number, return a list containing the two halves of the nubmer. If the
    number is odd, make the right most number higher.'''

# def number_split(n):
#     result_lst = []
#     if n % 2 == 0:
#         result_lst.append(n/2)
#         result_lst.append(n/2)
#         return result_lst
#     elif n % 2 != 0:
#         result_lst.append(n // 2)
#         result_lst.append(n // 2 + 1 )
#         return result_lst

def number_split(n):
    return [n//2, n - n//2]

print(number_split(4))
print(number_split(10))
print(number_split(11))
print(number_split(-9))