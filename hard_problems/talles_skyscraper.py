''' A city skyline can be represented as a 2-D list with 1s representing building. In the example
    below, the height of the tallest building is 4(second-most right column).

    [[0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1]]

    Create a function that takes a skyline(2-D list of 0's and 1's) and returns the height of the
    tallest skyscapers.'''

def tallest_skyscraper(lst):
    result = 0
    count = 0
    for i in lst: 
        if 1 in i:
            # return i.index(1)
            # return len(lst) - count
            return (len(lst) - count)
        count+=1

print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))

print(tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) )

print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]))
