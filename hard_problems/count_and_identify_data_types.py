''' Create a function that accepts unlimited argument, check and count how many data types are
    in those arguments. Finally return the total in a list.'''


def count_datatypes(*args):
	# new_lst = []
    i = 0
    s = 0
    b = 0
    l = 0
    t = 0
    d = 0
    for k in args:
        if type(k) == int:
            i+=1
        elif type(k) == str:
            s+=1
        elif type(k) == bool:
            b+=1
        elif type(k) == list:
            l+=1
        elif type(k) == tuple:
            t+=1
        elif type(k) == dict:
            d+=1
    return [i, s, b, l, t, d]

print(count_datatypes(1, 45, "Hi", False))
print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1))
print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23))
print(count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]))
