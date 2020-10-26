''' flip M to W '''

# def wumbo(words):
#     return words.replace("M", "W")

def wumbo(words):
    new_word = ''
    for i in words:
        if i == "M":
            i = "W"
        new_word += i
    return new_word

print(wumbo('MEET ME IN WARSAW'))
