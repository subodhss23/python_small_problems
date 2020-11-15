''' Create a function that takes a nubmer as input and return True if the sum of its digits has
    the same parity as the enritre number, Otherwise, return false.'''

def parity_analysis(num):
    new_str = str(num)
    sum = 0
    for i in new_str:
        sum+= int(i)
    if num % 2 == 0 and sum % 2 == 0 or num % 2 != 0 and sum % 2 != 0:
        return True
    else:
        return False

print(parity_analysis(243))
print(parity_analysis(12))
print(parity_analysis(3))