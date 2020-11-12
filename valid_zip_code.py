''' Zip codes consist of 5 consecutive digits. Given a string, write a function
    to determine whether the input is a valid zip code. A valid zip code is
    as follows:

        - Must only contain nubmers(no non-digits allowed)
        - Must not contain any spaces.
        - Must not be greater than 5 digits in length.
'''

def is_valid(zip_code):
    return zip_code.isdigit() and len(zip_code) == 5


print(is_valid('59001'))
print(is_valid("853a7"))
print(is_valid("732 32"))
print(is_valid('9081329'))