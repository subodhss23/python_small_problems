# create a function that takes in a two-dimensional list and returns the nubmer
# of sub-lists with only identical elements.

def count_identical(lst):
    len_set = 0
    counter = 0
    for i in lst:
        len_set = set(i)
        if len(len_set) == 1:
            counter+=1
    return counter

print(count_identical([
  [1],
  [2],
  [3],
  [4]
]))

print(count_identical([
  [1, 2],
  [2, 3],
  [3, 4],
  [4, 4]
]))

print(count_identical([
  [33, 33],
  [5],
  ["a", "a"],
  [2, 2, 2],
  [1, 2, 2],
  [3, 1]
]))

print(count_identical([
  ["@", "@", "@", "@"],
  [2, 3], [3, 4], [4, 4]
]))
