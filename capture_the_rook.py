''' Write a function that returns True if two rooks can attack each other,
    and False otherwise.'''

def can_capture(rooks):
    return rooks[0][0] == rooks[1][0] or rooks[0][1] == rooks[1][1]

print(can_capture(["A8", "E8"]))
print(can_capture(["A1", "B2"]))
print(can_capture(["H4", "H3"]))
print(can_capture(["F5", "C8"]))