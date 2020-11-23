''' Create a function that takes a list of names of superheros and superheroines and returns a list of
    only the names of superheroes ending in 'man' in alphabetical order. '''

def superheroes(heroes):
    new_lst = []
    for hero in heroes:
        if 'man' in hero and 'woman' not in hero.lower():
            new_lst.append(hero)
    return sorted(new_lst)

print(superheroes(["Batman", "Superman", "Spider-man", "Hulk", "Wolverine", "Wonder-Woman"]))
print(superheroes(["Catwoman", "Deadpool", "Dr.Strange", "Captain-America", "Aquaman", "Hawkeye"]))
print(superheroes(["Wonder-Woman", "Catwoman", "Invisible-Woman"]))