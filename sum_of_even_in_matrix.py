# Create a function that returns the sum of all even elements in a 2D matrix


def sum_of_evens(lst):
    sum = 0
    for i in lst:
        for j in i:
            if j % 2 == 0:
                sum += j
    return sum

print(sum_of_evens([
  [1, 0, 2],
  [5, 5, 7],
  [9, 4, 3]
]))

print(sum_of_evens([
  [1, 1],
  [1, 1]
]))

print(sum_of_evens([
  [42, 9],
  [16, 8]
])) 