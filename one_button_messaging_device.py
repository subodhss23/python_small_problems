''' Imagine a meaage device with only one button. For the letter A, you press the button one
    time, for E, you press it five times, for G, it's pressed seven times, etc, etc.

    Write a function that takes a string(the message) and returns the total nubmer of times the
    button is pressed. '''

def how_many_times(msg):
    counter = 0
    for i in msg:
        counter +=ord(i) - 96
    return counter

print(how_many_times('b'))
print(how_many_times("abde"))
# print(how_many_times("azy"))
# print(how_many_times("qudusayo"))