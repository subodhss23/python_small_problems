# messing around with dictionary 

my_dict = {
	"java": 100,
	"python": 112,
	"c": 11
}

# key_list = list(my_dict.keys())
# val_list = list(my_dict.values())

# print(key_list[val_list.index(100)])
# print(key_list[val_list.index(112)])
for name, value in my_dict.items():
	if value == 100:
		print(name)

print(max())