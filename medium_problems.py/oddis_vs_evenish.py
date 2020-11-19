''' Create a function that determines whether a nubmer is Oddish or Evenish. A number is 
Oddish if the sum of all of its digits is odd, and a number is Evenish if the sum of all 
of its digits is even. If a nubmer is oddish, return "Oddish". Otherwise, return "Evenish".
'''

def oddish_or_evenish(num):
    new_str = str(num)
    sum = 0
    for i in new_str:
        sum+=int(i)
    if sum % 2 == 0:
        return "Evenish"
    return "Oddish"

print(oddish_or_evenish(43))
print(oddish_or_evenish(373))
print(oddish_or_evenish(4433))