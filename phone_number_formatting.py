''' Create a function that takes a list of 10 numbers (between 0 and 9) and returns a string of those numbers 
    formatted as a phone number(e.g.(555)555-5555).'''

def format_phone_number(lst):
    new_str = "("
    for i in range(3):
        new_str+= str(lst[i])
    new_str+= ') '
    for i in range(3,6):
        new_str+= str(lst[i])
    new_str+= '-'
    for i in range(6, 10):
        new_str+=str(lst[i])
    return new_str

print(format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))