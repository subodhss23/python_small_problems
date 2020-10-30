''' convert list into string '''

def list_to_string(lst):
    # new_str = ""
    # for i in lst:
    #     new_str += str(i)
    # return new_str
    new_lst = str(lst)
    return ("".join(new_lst))

print(list_to_string([1, 2, 3, 4, 5, 6]))
print(list_to_string(["a", "b", "c", "d", "e", "f"]))
print(list_to_string([1, 2, 3, "a", "s", "dAAAA"]))