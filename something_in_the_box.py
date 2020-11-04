# create a function that returns True if an asterisk * is inside the box.

def in_box(lst):
	for i in lst:
		if i[0] == '*' or i[len(i) - 1] == "*":
			return False
		else:
			if '*' in i:
				return True
	return False




print(in_box([
  "###",
  "#*#",
  "###"
]))

print(in_box([
  "####",
  "#* #",
  "#  #",
  "####"
]) )

print(in_box([
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
]) )

print(in_box([
	"*####",
	"# #",
	"# #*",
	"####" 
]))