''' Create a function that takes a list as an argument and returns a new nested
    list for each element in the orginal list. The nested list must be filled with the 
    corresponding element(string or nubmer) in the orginal list and each nested list
    has the same amount of elements as the orginal list.'''


def multiply(l):
    list_one = []
    for i in l:
        counter = 0
        new_list = []
        while(counter < len(l)): 
            new_list.append(i)
            counter+=1
        list_one.append(new_list)
    return list_one


print(multiply([4, 5]))
print(multiply(["*", "%", "$"]))
print(multiply(["A", "B", "C", "D", "E"]))