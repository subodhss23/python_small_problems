''' Create a function that takes three values:
    
    - h hours
    - m minutes
    - s seconds

    Return the value that's the longest duration. '''


def longest_time(h, m, s):
    hour = h * 60 * 60
    min = m * 60
    sec = s
    new_lst = [hour, min, sec]
    if max(new_lst) == hour:
        return h
    elif max(new_lst) == min:
        return m
    elif max(new_lst) == sec:
        return s

print(longest_time(1, 59, 3598))
print(longest_time(2, 300, 15000))
print(longest_time(15, 955, 59400))