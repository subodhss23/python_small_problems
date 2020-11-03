''' create a function that returns the total number of steps it takes to transform
    each element to the maximal element in the list. Each step consists of incrementing 
    a didit by one. '''


def increment_to_top(lst):
    counter = 0
    for i in lst:
        while i < max(lst)
            i+=1
            counter+=1
    return counter
    

print(increment_to_top([3,4,5]))
print(increment_to_top([4,3,4]))
print(increment_to_top([3,3,3]))
print(increment_to_top([3,10,3]))