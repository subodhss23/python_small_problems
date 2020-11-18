''' Given a sentence, create a function that replaces every 'a' with 'an absolute'. It should return the
    string itself if it doesn't have any 'a'.'''

def absolute(txt):
    result_arr = []
    txt_to_lst = txt.split(' ')
    for i in txt_to_lst:
        if i.lower() == 'a':
            result_arr.append('an absolute')
        else:
            result_arr.append(i)
    return (' ').join(result_arr).capitalize()


print(absolute("I am a champion!!!"))
print(absolute("Such an amazing bowler."))
print(absolute("A man with no haters."))
