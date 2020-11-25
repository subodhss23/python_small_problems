''' Given a sentence as txt, return True if any two adjacent words have this property: One word ends
    with a vowel, while the word immediately after begins with a vowel( a e i o u ).'''

def vowel_links(txt):
    new_lst = txt.split(' ')
    vowel = 'aeiou'
    for i in range(len(new_lst)-1):
        if new_lst[i][-1] in vowel and new_lst[i+1][0] in vowel:
            return True
    return False

print(vowel_links("a very large appliance"))
print(vowel_links("go to edabit"))
print(vowel_links("an open fire"))
print(vowel_links("a sudden applause"))