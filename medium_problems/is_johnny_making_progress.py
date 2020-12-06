''' To train for an upcoming marathon, Johnny goes on one long-distance run each Saturday. He wants to
    track how often the number of miles he run exceeds the previous Saturday. This is called a progress day.

    Create a function that takes in al ist of miles run every Saturday and returns Johnny's total
    number of progess days.'''

def progress_days(runs):
    result = 0
    for i in range(1, len(runs)):
        if runs[i] > runs[i-1]:
            result+=1
    return result

print(progress_days([3, 4, 1, 2]) )
print(progress_days([10, 11, 12, 9, 10]))
print(progress_days([6, 5, 4, 3, 2, 9]))
print(progress_days([9, 9]))