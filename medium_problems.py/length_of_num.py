''' Create a function that takes a number num and returns its length.'''

def number_length(num):
    num_str = str(num)
    count = 0
    for i in num_str:
        count+=1
    return count

print(number_length(10))
print(number_length(5000))
print(number_length(0))