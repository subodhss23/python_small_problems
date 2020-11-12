''' Create a function that takes the number of daily average recovered cases
    recovered cases recovers, daily average new_cases, current active_cases,
    and returns the number of days it will take to reach zero cases.'''

import math
def end_corona(recovers, new_cases, active_cases):
    return math.ceil(active_cases / (recovers - new_cases))


print(end_corona(4000, 2000, 77000))
print(end_corona(3000, 2000, 50699))
print(end_corona(30000, 25000, 390205))