''' Write a function that changes every letter to the next letter:

    - "a" becomes 'b"
    - "b" becomes 'c'
    - and so on '''

def move(word):
    new_str = ''
    for i in word:
        new_str+= chr(ord(i)+1)
    return new_str

print(move('whatup'))
print(move('welcomeb'))
