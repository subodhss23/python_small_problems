# create a function that takes a list of numbers and returns the second largest 
# number

def second_largest(lst):
    return sorted(lst)[-2]
    
print(second_largest([2,3,8,7,9,5,6]))