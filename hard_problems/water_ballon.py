''' Once a water ballon pops, is soaks the area around it. The ground gets drier the further away you travel from the balloon.

    The effect of a water balloon popping can be modeled using a list. Create a function that takes a list which takes the pre-pop
    state and returns the state after the balloon is popped. The pre-pop state will contain at most a single ballon, whose size is 
    represented by the only non-zero element.'''

def pop(lst):
    impact = lst[len(lst)//2]
    new_lst = [0]
    for i in range(1, impact+1):
        new_lst.append(i)
    return new_lst[:-1] + new_lst[::-1]

print(pop([0, 0, 0, 0, 4, 0, 0, 0, 0]))
print(pop([0, 0, 0, 3, 0, 0, 0]))
print(pop([0, 0, 2, 0, 0]) )
print(pop([0]))