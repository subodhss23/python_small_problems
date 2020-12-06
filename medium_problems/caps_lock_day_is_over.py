''' October 22nd is CAPS LOCK DAY. Apart from the day, every senctence shoudl be lowercase, so write a function
    to normalize a sentence.

    Create a function that takes a string. If the string is all uppercase characters, convert it to lowercase
    and add an exclamation mark at the end.'''

def normalize(txt):
    if (txt[-1]) == '.':
        return txt[:-1].capitalize() + '!'
    return txt.capitalize() + '!'

print(normalize("CAPS LOCK DAY IS OVER"))
print(normalize("Today is not caps lock day."))
print(normalize("WE WANT THIS COVID THING TO BE OVER"))
print(normalize("Let us stay calm, no need to panic."))