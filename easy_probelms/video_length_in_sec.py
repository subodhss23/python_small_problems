''' You are given the lenth of a video in minutes. The format is mm::ss(e.g: "02:54).
    Create a function that takes the video length and return it in seconds.'''

def minutes_to_seconds(time):
    new_lst =time.split(':')
    if int(new_lst[1]) >= 60:
        return False
    result = int(new_lst[0]) * 60 + int(new_lst[1])
    return result 


print(minutes_to_seconds("01:00"))
print(minutes_to_seconds("13:56"))
print(minutes_to_seconds("10:60"))
