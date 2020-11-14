''' Write a function that takes a string as an argument and returns the left
    most integer in the string.'''

def left_digit(num):
    for i in num:
        if i.isdigit():
            return int(i)

print(left_digit("TrAdE2W1n95!"))
print(left_digit("V3r1ta$"))