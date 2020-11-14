''' calcualte the distance, turn negative in positive '''

def marathon_distance(d):
    sum = 0
    for i in d:
        sum+=abs(i)
    return sum == 25

print(marathon_distance([1, 2, 3, 4]))
print(marathon_distance([1, 9, 5, 8, 2]) )
print(marathon_distance([-6, 15, 4]))