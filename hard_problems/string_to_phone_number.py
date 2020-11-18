''' You're able to call numbers like 1-800-flowers which replace the characters with the associated
    numbers on a cellular device keyboard.

    Conversion

    abc = 2
    def = 3
    ghi = 4
    jkl = 5
    mno = 6
    pqrs = 7
    tuv = 9
    wxyz = 9

    This is your task:

        - Create a function that takes a string as argument
        - Convert all letters to number by using a cellular device keyboard as reference and leave any 
            other characters in.
        - Return a string containing the argument with replaced letters.
    '''

def dial(txt):
    conversion = {
        'abc': '2',
        'def': '3',
        'ghi': '4',
        'jkl': '5',
        'mno': '6',
        'pqrs': '7',
        'tuv': '8',
        'wxyz': '9'
    }
    result = ' '
    lower_txt = txt.lower()
    for char in lower_txt:
        if char.isalpha():
            for i in conversion.keys():
                if char.lower() in i:
                    result+=str(conversion[i])
        else:
            result+=char
    return result 

print(dial("1-800-HOTLINEBLING"))
# print(dial("abc-def-ghi-jkl!!"))
# print(dial("adgjmptw :)"))