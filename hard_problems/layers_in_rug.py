''' Write a function that counts how many concentric layers a rug.'''


def count_layers(rug):
    layers = []
    count = 0
    for layer in rug:
        if layer not in layers:
            layers.append(layer)
    return len(layers)

print(count_layers([
  "AAAA",
  "ABBA",
  "AAAA"
]))

print(count_layers([
  "AAAAAAAAA",
  "ABBBBBBBA",
  "ABBAAABBA",
  "ABBBBBBBA",
  "AAAAAAAAA"
]))

print(count_layers([
  "AAAAAAAAAAA",
  "AABBBBBBBAA",
  "AABCCCCCBAA",
  "AABCAAACBAA",
  "AABCADACBAA",
  "AABCAAACBAA",
  "AABCCCCCBAA",
  "AABBBBBBBAA",
  "AAAAAAAAAAA"
]))
