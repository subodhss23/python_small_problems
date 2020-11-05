''' Given three arguments = a dictionary d1, a key name and a value - return an object with
    that name and value in it(as key-value pairs.) '''


def add_name(obj, name, value):
    obj.update({name : value})
    return obj
    
print(add_name({}, "Brutus", 300))
print(add_name({ "piano": 500 }, "Brutus", 400))
print(add_name({ "piano": 500, "stereo": 300 }, "Caligula", 440))