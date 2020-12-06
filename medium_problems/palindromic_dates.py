''' The 2nd of Feburary 2020 is a palindromic date in both dd/mm/yyyy and mm/dd/yyy format
    (02/02/2020). Given a date in dd/mm/yyyy format, return True if the date is palindromic
    in both date formats, otherwise return False. '''


def palindromic_date(date):
    new_date = ('').join(date.split('/'))
    return new_date == new_date[::-1] and new_date[0:2] == date[3:5]
    

print(palindromic_date("02/02/2020"))
print(palindromic_date("11/12/2019"))
print(palindromic_date("11/02/2011"))