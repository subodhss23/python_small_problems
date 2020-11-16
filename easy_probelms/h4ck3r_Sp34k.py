''' Create a function that takes a string as an argument and
    returns a code (h4ck3r 5p34k) version of the string.'''

def hacker_speak(txt):
    new_str = ''
    for i in txt:
        if i == 'a':
            i = '4'
            new_str+=i
        elif i == 'e':
            i = '3'
            new_str+=i
        elif i == 'i':
            i = '1'
            new_str+=i
        elif i == 'o':
            i = '0'
            new_str+=i
        elif i == 's':
            i = '5'
            new_str+=i
        else:
            new_str+=i
    return new_str

print(hacker_speak("javascript is cool"))
print(hacker_speak("programming is fun"))
print(hacker_speak("become a coder") )