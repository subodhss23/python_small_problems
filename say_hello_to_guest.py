''' In this exercise you will have to:
    1. Take a list of names.
    2. Add "Hello" to every name.
    3. Make one big string with all greetings.

    The solution should be one string with a comma in between every "Hello (Name)". '''

def greet_people(names):
    new_str = ''
    for i in range(0, len(names)):
        print(i)
        if i <= len(names) - 2 :
            new_str+="Hello " +names[i] + ', '
        elif i == len(names) - 1 :
            new_str+="Hello " +names[i]
            print('we are here')
    return new_str

print(greet_people(["Dave", "Alica" , "Sam"]))