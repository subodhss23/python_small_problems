''' Create a function that check if the box is completely filled with the
    asterisk symbol * 
'''

def completely_filled(lst):
    for i in lst:
        if ' ' in i:
            return False
    return True

print(completely_filled([
  "#####",
  "#***#",
  "#***#",
  "#***#",
  "#####"
]))

print(completely_filled([
  "#####",
  "#* *#",
  "#***#",
  "#***#",
  "#####"
]))

print(completely_filled([
  "###",
  "#*#",
  "###"
]))

print(completely_filled([
  "##",
  "##"
]))