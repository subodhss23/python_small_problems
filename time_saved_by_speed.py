''' create a function that calcualtes the amount of time saved were 
    you traveling with an average speed tat is above the speed-limit as compared
    to traveling with an average speed exactly at the speed-limit.'''

def time_saved(s_lim, s_avg, d):
    normal_time = (d / s_lim) * 60
    going_fast = (d / s_avg) * 60
    saved_time = normal_time - going_fast
    return round(saved_time, 1)


print(time_saved(80, 90, 40))
print(time_saved(80, 90, 4000))
print(time_saved(80, 100, 40 ))
print(time_saved(80, 100, 10))