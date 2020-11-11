''' create a function that accepts a string as an arguement and returns the first
    non-repeated characters.'''

def first_non_repeated_character(txt):
    new_lst = list(txt)
    search_duplicate = []
    for i in new_lst: 
            if new_lst.count(i) == 1:
                return i
    return False
            

print(first_non_repeated_character("g"))
print(first_non_repeated_character("it was then the frothy word met the round night"))
print(first_non_repeated_character("the quick brown fox jumps then quickly blows air"))
print(first_non_repeated_character("hheelloo"))
print(first_non_repeated_character(""))