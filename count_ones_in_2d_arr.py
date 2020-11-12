# Create a function to count the nubmer of 1s in a 2D list.

def count_ones(lst):
    count = 0
    for i in lst:
        count+= i.count(1)
    return count

print(count_ones([
  [1, 0],
  [0, 0]
]))

print(count_ones([
  [1, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]))

print(count_ones([
  [1, 2, 3],
  [0, 2, 1],
  [5, 7, 33]
]))