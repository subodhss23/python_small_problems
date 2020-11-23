''' IN this challenge, rage given number to the power of 2 and find occurance of '666'

    - 'Safe' if n is not apocalyptic
    - 'Single' if into 2^n there's a single occurence of 666
    - 'double' if into 2^n there are two occurence of 666
    - 'tiple' if into 2^n there are three occurence of 666. '''

def is_apocalyptic(number):
    new_num = str(2 ** number)
    replaced_num = new_num.replace('666', 'found')
    if replaced_num.count('found') == 0:
        return 'Safe'
    elif replaced_num.count('found') == 1:
        return 'Single'
    elif replaced_num.count('found') == 2:
        return 'Double'
    elif replaced_num.count('found') == 3:
        return 'Triple'

print(is_apocalyptic(66))
print(is_apocalyptic(157))
print(is_apocalyptic(220))
print(is_apocalyptic(931))
