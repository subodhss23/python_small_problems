''' create a function that takes a list as an argument and returns True or False depending on whether
    the average of all elements in the list is a whole number or not. '''

def is_avg_whole(arr):
    sum = 0
    for i in arr:
        sum+=i
    avg = sum/len(arr)
    return avg == int(avg)

print(is_avg_whole([1,3]))
print(is_avg_whole([1,2,3,4]))