'''Write a function that reeverses all the words in a sentence that start with
    a particular letter.'''

def special_reverse(s, c):
    result_lst = []
    new_lst = s.split(' ')
    for i in new_lst:
        if i[0] == c:
            result_lst.append(i[::-1])
        else:
            result_lst.append(i)
    return (' ').join(result_lst)

print(special_reverse("word searches are super fun", "s"))
print(special_reverse("first man to walk on the moon", "m"))
print(special_reverse("peter piper picked pickled peppers", "p"))