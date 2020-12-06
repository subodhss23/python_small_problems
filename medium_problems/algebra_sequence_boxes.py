''' Create a function that takesa number(step) as an argument and returns the amount
    of boxes in that step of the sequence. '''

def box_seq(step):
    if step%2==0:
        return step
    else:
        return step + 2

print(box_seq(0))
print(box_seq(1))
print(box_seq(2))
