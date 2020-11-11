''' Write a function that takes two lists and adds the first elements in the first
    list with the first element in the second list, the second element in the first 
    list with the second element in the second list, etc. Return True if all element
    combinations add up to the same number. Otherwise, return False. '''

def puzzle_pieces(a1, a2):
    new_lst = []
    sum = 0
    if len(a1) == len(a2):
        for i in range(len(a1)):
            sum = a1[i] + a2[i]
            new_lst.append(sum)
        new_set = set(new_lst)
        return len(new_set) == 1
    return False

print(puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]))
print(puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]))
print(puzzle_pieces([1, 2], [-1, -1]))
print(puzzle_pieces([9, 8, 7], [7, 8, 9, 10]))