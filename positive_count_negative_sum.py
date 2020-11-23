''' Create a function that takes a list of positive and negative numbers. Return a list where the first element
    is the count of positive numbers and the second element is the sum of negative numbers. '''


def sum_neg(lst):
    count = 0
    sum = 0
    new_lst = []
    for i in lst:
        if i >= 0:
            count += 1
        elif i < 0:
            sum += i
    new_lst.append(count)
    new_lst.append(sum)
    if count == 0 and sum == 0:
        return []
    return new_lst


print(sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]))
print(sum_neg([91, -4, 80, -73, -28]))
print(sum_neg([]))
