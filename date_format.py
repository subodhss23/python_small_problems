# create a function that converst a date formatted as MM/DD/YYYY TO YYYYDDMM.

def format_date(date):
    m, d, y = date.split('/')
    return ''.join((y,d,m))

print(format_date("11/12/2019"))
print(format_date("12/31/2019"))
print(format_date("01/15/2019"))