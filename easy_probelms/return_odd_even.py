''' Given a list, return True if there are more odd nubmers than even nubmers,
    otherwise return False'''

def oddeven(lst):
    odd = 0
    even = 0
    for i in lst:
        if i % 2 == 0:
            even+=1
        else:
            odd+=1
    return odd > even

print(oddeven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(oddeven([1]))
print(oddeven([13452394823795273847528572346]))
