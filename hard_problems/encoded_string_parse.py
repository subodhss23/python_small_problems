''' Create a function which takes in an encoded string and returns a dictonary according to the follwing
    example:

    parse_code("John000Doe000123") ➞ {
        "first_name": "John",
        "last_name": "Doe",
        "id": "123"
    }

    parse_code("michael0smith004331") ➞ {
        "first_name": "michael",
        "last_name": "smith",
        "id": "4331"
    }

    parse_code("Thomas00LEE0000043") ➞ {
        "first_name": "Thomas",
        "last_name": "LEE",
        "id": "43"
    } '''


def parse_code(txt):
    final_arr = []
    new_obj = {
        "first_name": "",
        "last_name": "",
        "id":""
    }
    new_arr = txt.split('0')
    for i in new_arr:
        if i != '':
            final_arr.append(i)
    new_obj["first_name"] = final_arr[0]
    new_obj["last_name"] = final_arr[1]
    new_obj["id"] = final_arr[2]
    return new_obj


print(parse_code("John000Doe000123"))
print(parse_code('Michael0Smith004331'))
print(parse_code('Thomas0000Lee0000045553'))
print(parse_code('a0b01'))