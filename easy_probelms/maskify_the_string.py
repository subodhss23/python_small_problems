'''Usually when you sign up for an account to by something, your credit card number, phone number
    or anser to a secret question is partially obscured in some way. Since someone could look over
    your shoulder, you don't want that shown on your screen. Hence, the website masks these strings.

    YOu task is to create a function that takes a string, transforms all but the last four characters
    into '#' and return  new masked string. '''

def maskify(txt):
    temp_four = ''
    if len(txt) <= 4:
        return txt
    else:
        temp_four = txt[-4:]
        return (len(txt) - 4)*'#'+ temp_four


print(maskify("4556364607935616"))
print(maskify("64607935616"))
print(maskify("1"))
print(maskify(""))