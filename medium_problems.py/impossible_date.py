''' Given the parameters day, month and year, return whether that date is a valid date.'''

import datetime

def is_valid_date(d, m, y):
    try:
        (datetime.datetime(y, m, d))
        return True
    except ValueError:
        return False
        
print(is_valid_date(35, 2, 2020))
print(is_valid_date(8, 3, 2020))
print(is_valid_date(31, 6, 1980))