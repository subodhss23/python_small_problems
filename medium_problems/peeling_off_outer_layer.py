''' Given a list of lists, return a new list of lists containing every element, except for 
    the outer elements.'''

def peel_layer_off(lst):
    if len(lst) <= 2:
        return []
    else:
        newlst = []
        middle_layer = lst[1:-1]
        for x in range(len(middle_layer)):
            middle_layer[x].pop()
            a = middle_layer
        for x in range(len(a)):
            newlst.append(a[x][1:])
    return newlst


print(peel_layer_off([
  ["a", "b", "c", "d"],
  ["e", "f", "g", "h"],
  ["i", "j", "k", "l"],
  ["m", "n", "o", "p"]
]))

print(peel_layer_off([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25],
  [26, 27, 28, 29, 30],
  [31, 32, 33, 34, 35]
]))

print(peel_layer_off([
  [True, False, True],
  [False, False, True],
  [True, True, True]
]))