# Create a function that determines if there is an upward trend. 
def upward_trend(lst):
    for i in lst:
        if type(i) == str:
            return 'Strings not permitted!'
    return lst == sorted(lst)
    

print(upward_trend([1, 2, 3, 4]))
print(upward_trend([1, 2, 6, 5, 7, 8]))
print(upward_trend([1, 2, 3, "4"]))
# print(upward_trend([1, 2, 3, 6, 7]))