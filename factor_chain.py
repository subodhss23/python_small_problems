''' A factor chain is a list where each previous element is a factor of the next
    consecutive elemnt.
    The following is a factor chain:
    [3, 6,12, 36]
    '''

def factor_chain(lst):
    i = len(lst) - 1
    while i >= 1:
        if lst[i] % lst[i -1] != 0:
            i -= 1   
            return False
        return True



print(factor_chain([1, 2, 4, 8, 16, 32]))
print(factor_chain([1, 1, 1, 1, 1, 1]) )
print(factor_chain([2, 4, 6, 7, 12]) )
print(factor_chain([10, 1]))