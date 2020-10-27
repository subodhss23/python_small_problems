# create a function that takes a string and returns the letters 
# occur only once

def find_letters(words):
    lst = []
    counter = 0
    for i in words:
        counter = words.count(i)
        if counter == 1:
            lst.append(i)
    return lst

print(find_letters("monopoly"))
print(find_letters("balloon"))
print(find_letters("analysis"))