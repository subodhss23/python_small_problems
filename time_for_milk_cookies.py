''' Christmas Eve is almost upon us, so naturally we need to prepare some milk
    and cookies for Santa! Create a function that accepts a Date object and returns
    True if it's Christmas Eve (December 24th) and False otherwise. '''

import datetime
def time_for_milk_and_cookies(date):
    return date.month == 12 and date.day == 24

print(time_for_milk_and_cookies(datetime.date(2013, 12, 24)))
print(time_for_milk_and_cookies(datetime.date(2013, 1, 23)))
print(time_for_milk_and_cookies(datetime.date(3000, 12, 24)))