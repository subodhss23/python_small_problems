''' Given a string worm create a function that takes the length of the worm and converts it
    into millimeters. Each - represents one centimeter.'''

def worm_length(worm):
    sum = 0
    MIL = 10
    if worm == '':
        return 'invalid'
    for i in worm:
        if i != '-':
            return 'invalid'
        sum+=1
    return str(sum * MIL)+' mm'
       

print(worm_length("----------"))
print(worm_length(""))
print(worm_length("---_-___---_"))