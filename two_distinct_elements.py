''' In each input list, every number repeats at least once, except for two. 
    Write a function that returns the two unique numbers. '''


def return_unique(lst):
    result = []
    counter = 0
    for i in lst:
        head = i
        while (counter <= len(lst)):
            if head != lst[counter]:
                result.append(head)
                counter += 1
    return result

            
        




print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
# print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
# print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))