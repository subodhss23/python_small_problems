''' Write a function that converts a dictionary into a list of keys-values tuples.'''

def dict_to_list(d):
    new_lst = []
    return sorted(list(d.items()))

print(dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}))

print(dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) )