''' Write a function that reverse a string. Make your function recursive.'''

def reverse(txt):
    if txt == '':
        return txt
    else:
        return reverse(txt[1:]) + txt[0]

print(reverse('what'))
print(reverse('dont hack me'))