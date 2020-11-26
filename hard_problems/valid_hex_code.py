''' Create a function that determines whether a string is a valid hex code. 

    A hex code must begin with a pound key # and is exactly 6 characters in length. Each character must be a digit
    from  0-9 or an alphabetic character from A-F. All alphabetic characters may be uppercase or lowercase. '''

def is_valid_hex_code(txt):
    new_txt = txt[1:7]
    hex_alpha = 'ABCDEFabcdef'
    if len(txt) == 7 and txt[0] == '#':
        for i in range(len(new_txt)):
            if new_txt[i].isdigit() == False and new_txt[i] not in hex_alpha:
                return False   
        return True
    return True           


print(is_valid_hex_code("#CD5C5C"))
# print(is_valid_hex_code("#EAECEE"))
# print(is_valid_hex_code("#eaecee"))
# print(is_valid_hex_code("#CD5C58C"))
print(is_valid_hex_code("#CD5C5Z"))
# print(is_valid_hex_code("#CD5C&C"))
# print(is_valid_hex_code("CD5C5C"))