''' A number n in apocalyptic if 2^n contains a string of 3 consecutive 6s (666 being the
    presumptive "number of the beast")

    Create a function that takes a number n as input. If the number is apocalytic, find the index of
    666 in 2^n, return "Repent! X days until the Apocalypse!" (X being the index). If not, returns
    "Crisis averted. Resume sinning."'''


def apocalyptic(n):
    new_n = str(2**n)
    if '666' in new_n:
        new_index =  new_n.index('666')
        return "Repent! " + str(new_index) + " days until the Apocalypse!"
    else:
        return "Crisis averted. Resume sinning."


print(apocalyptic(109))
print(apocalyptic(157))
print(apocalyptic(175))
print(apocalyptic(220))