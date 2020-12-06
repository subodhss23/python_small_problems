''' The challenge is to create the functionality of the title() method into a 
    function called emphasise(). The title() method capitalises the first letter
    of every word and lowercases all of the other letters in the word.'''


def emphasise(txt):
    new_lst = txt.split(' ')
    result_lst = []
    if len(txt) == 0:
        return ''
    else:
        for i in range(len(new_lst) ):
            result_lst.append(new_lst[i][0].capitalize() + new_lst[i][1:].lower())
        return (' ').join(result_lst)

print(emphasise("hello world"))
print(emphasise("GOOD MORNING"))
print(emphasise("99 red balloons!"))