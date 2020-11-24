''' Given a list of directions to spin ,"left" or "right", return an integer of how many full 360 rotations were made. 
    Note that each word in the list counts as a 90 rotation in that direction.'''

def spin_around(lst):
	angle = 0
	for i in lst:
		if i == "right":
			angle+=90
		elif i == "left":
			angle-=90
	absangle = abs(angle)
	turns = absangle/360
	print (int(turns))
	return int(turns)

print(spin_around(["left", "right", "left", "right"]))
print(spin_around(["right", "right", "right", "right", "right", "right", "right", "right"]) )
print(spin_around(["left", "left", "left", "left"]))