'''create a function that takes a string(will be a person's first and last name)
and returns a string with the first and last name swapped.'''

def name_shuffle(txt):
    tmp_lst = []
    tmp_var = ''
    for i in txt:
        tmp_var+=i
        if i == ' ':
            tmp_lst.append(tmp_var)
    return tmp_lst

print(name_shuffle("Subodh Sharma"))
print(name_shuffle("Ram chandra"))