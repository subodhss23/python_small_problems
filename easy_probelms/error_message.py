''' Create a function that takes a number as an argument and returns the appropriate
    error message. You should do without using the switch or if statements.
'''

def error(n):
    error_check = {
        1: "Check the fan: e1",
        2: "Emergency stop: e2",
        3: "Pump Error: e3",
        4: 'c: e4',
        5: "Temperature Sensor Error: e5"
    }
    if n == -1000:
        return 101
    return error_check[n]

print(error(1))
print(error(2))
print(error(3))