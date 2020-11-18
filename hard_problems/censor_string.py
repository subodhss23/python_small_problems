''' Someone has attempted to censor my strings by replacing every vowel with a *, l*k*th*s. Luckily, I've
    been able to find the vowels that were removed. 

    Given a censored string and a string of the censored vowels, return the orginal uncensored string.'''

def uncensor(txt, vowels):
    new_string = ''
    counter = 0
    for i in txt:
        if i == '*':
            new_string+=vowels[counter]
            counter+=1
        else:
            new_string+=i
    return new_string

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("abcd", ""))
print(uncensor("*PP*RC*S*", "UEAE"))