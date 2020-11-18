''' Given the month and year as numbers return whether the month contains
    a Friday 13th.'''
from datetime import date
def has_friday_13(month, year):
    thirteenth = date( year, month, 13)
    return thirteenth.weekday() == 4



print(has_friday_13(3, 2020))
print(has_friday_13(10, 2017))
print(has_friday_13(1, 1985))