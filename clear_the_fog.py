''' Create a function which returns the word in the string, but with all the fog letters removed. 
    However, if the string is clear from fog, return "It's a clear day!"'''

def clear_fog(txt):
    if 'f' not in txt:
        return "It's a clear day!"
    else:
        for i in txt:
            if i.lower() in "fog":
                txt = txt.replace(i,'')
    return txt

print(clear_fog("fogfogFFfoooofftogffreogffesGgfOogfog"))
print(clear_fog("what is up"))