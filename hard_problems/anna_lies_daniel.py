'''Anna is a strange girl. She likes certain boys, but not others. 
    You have to figure out why she likes some, and not the others. '''

def anna_likes(boy):
    vowel = 'aeiouAEIOU'
    count = 0
    for i in boy:
        if i in vowel:
            count+=1
    print(len(boy))
    print(count)
    print(len(boy) - count)
    return count == len(boy) - count

print(anna_likes("David"))
print(anna_likes("Samuel"))
print(anna_likes("Gary"))