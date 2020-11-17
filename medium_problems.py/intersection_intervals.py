''' Create a function that takes in a list of intervals and returns how many intervals overlap
    with a given point.

    An interval overlaps a particular point if the point exists inside the interval, or on the
    interval's boundary. For example the point 3 overlaps with the interval [2,4](it is inside)
    and [2,3](it is on the boundary).'''

def count_overlapping(intervals, point):
    counter = 0
    for i in intervals:
        if point >= i[0] and point <= i[1]:
            counter+=1
    return counter


print(count_overlapping([[1, 2], [2, 3], [3, 4]], 5))
print(count_overlapping([[1, 2], [5, 6], [5, 7]], 5))
print(count_overlapping([[1, 2], [5, 8], [6, 9]], 7))