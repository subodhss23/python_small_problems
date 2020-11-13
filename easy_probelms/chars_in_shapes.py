''' Create a function to calculate how many characters in total are needed to make
    up the shape. You will be given a list of strings which make up a shape in the
    compiler(i.e. a square, a rectangle or a line).
'''

def count_characters(lst):
    count = 0
    for i in lst:
        count+= len(i)
    return count

print(count_characters([
  "###",
  "###",
  "###"
]) )

print(count_characters([
  "22222222",
  "22222222",
]) )

print(count_characters([
  "------------------"
]) )

print(count_characters(["", ""]))