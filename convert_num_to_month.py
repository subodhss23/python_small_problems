''' Create a function that takes a number(from 1 10 12) and returns its corresponding
    month name as a sting. '''

def month_name(num):
    months={
        '1':"January",
        '2':"February",
        '3':"March",
        '4':"April",
        '5':"May",
        '6':"June",
        '7':"July",
        '8':"August",
        '9':"September",
        '10':"October",
        '11':"November",
        '12':"December"
    }
    return months[str(num)]

print(month_name(3))
print(month_name(12))
print(month_name(6))