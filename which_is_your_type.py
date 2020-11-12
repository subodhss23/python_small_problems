# convert data type B into data type A

def convert(data1, data2):
    new_data_type = type(data1)
    return new_data_type(data2)

print(convert([1, 2, 4, 8], (7, 8, 9)))
print(convert((7, 8, 9), [1, 2, 4, 8]))
print(convert([1, 2, 4, 8], {2, 3, 5, 7, 11, 13}) )
print(convert({2, 3, 5, 7, 11, 13}, [1, 2, 4, 8])