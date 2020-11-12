'''Given a list of women and a list of men, either:
    - Return "sizes don't match" if the two lists have different sizes.
    - If the sizes match, return a list of pairs, with the first woman paired
        with the first man, second woman paired with the second man, etc.'''


def zip_it(women, men):
    if len(women) == len(men):
        result =  zip(women, men)
        return list(result)
    return "sizes don't match"


print(zip_it(["Elise", "Mary"], ["John", "Rick"]))
print(zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh"]))
print(zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh", "Tim"]))