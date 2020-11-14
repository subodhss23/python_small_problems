''' Removing enemies from the list of people, even if the enemy shows up twice.'''

def remove_enemies(names, enemies):
    new_lst = []
    for i in names:
        if i not in enemies:
            new_lst.append(i)
    return new_lst

print(remove_enemies(["Fred"], []))
print(remove_enemies(["Adam", "Emmy", "Tanya", "Emmy"], ["Emmy"]))
print(remove_enemies(["John", "Emily", "Steve", "Sam"], ["Sam", "John"]))