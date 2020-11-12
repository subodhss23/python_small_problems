''' Sam and Frodo need to be close. If they are side by side in the list, your function should
    return True. If there is a name between them , return False.'''

def middle_earth(lst):
    if 'Frodo' and 'Sam' in lst:
        return abs(lst.index('Frodo') - lst.index('Sam')) == 1

print(middle_earth(["Frodo", "Sam", "Gandalf"]))
print(middle_earth(["Frodo", "Saruman", "Sam"]))
print(middle_earth(["Orc", "Sam", "Frodo", "Legolas"]))