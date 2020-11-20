'''Create a function that returns the number of characters shared between two words.'''

def shared_letters(txt1, txt2):
    count = 0
    for i in set(txt1):
        if i in txt2:
            count+=1
    return count

print(shared_letters("apple", "meaty"))
print(shared_letters("fan", "forsook"))
print(shared_letters("spout", "shout"))
print(shared_letters("class", "last"))