''' Create a function that changes specific words into emoticons. Given a sentence as a string,
    replace the words smile, grin, sad and mad with their corresponding emoticons.'''

def emotify(txt):
    lst = txt.split(' ')
    emoti = {
        "smile": ":D",
        "grin":":)",
        "sad": ":(",
        "mad": ":P"
    }
    return "Make me " + emoti[lst[2]]

print(emotify("Make me smile"))
print(emotify("Make me grin"))
print(emotify("Make me sad"))