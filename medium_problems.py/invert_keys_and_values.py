''' Write a function that inverts the keys and values of a dictionary.'''

def invert(dct):
   new_dict = dict(zip(dct.values(), dct.keys()))
   return new_dict

# def invert(d):
#     return {v: k for k, v in d.items()}

print(invert({ "z": "q", "w": "f" }))
