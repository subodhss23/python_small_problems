''' Write a function that retrives all words that begin with a vowel.'''

def retrieve(txt):
    vowel = 'aeiou'
    lst = txt.lower().strip('.').split(' ')
    new_lst = []
    if txt == '':
        return new_lst
    else:
        for i in lst:
            if i[0] in vowel:
                new_lst.append(i)
    return new_lst

print(retrieve("A simple life is a happy life for me."))
print(retrieve("Exercising is a healthy way to burn off energy."))
print(retrieve("The poor ostrich was ostracized."))
print(retrieve(""))