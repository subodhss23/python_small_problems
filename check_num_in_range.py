''' Given a number and a dictionary with min and max properties, return True if the number
    lies within the given range(inclusive). '''

def is_in_range(n, r):
    return n >= r["min"] and n <= r["max"]
        

print(is_in_range(4, { "min": 0, "max": 5 }))
print(is_in_range(4, { "min": 4, "max": 5 }))
print(is_in_range(4, { "min": 6, "max": 10 }))
print(is_in_range(5, { "min": 5, "max": 5 }))