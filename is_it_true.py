# write a function that compares relaltion within a string
# eg "2=2" "8<7"

def is_it_true(relation):
    new_str = ""
    if "=" in relation:
        new_str = relation.replace("=", "==")
        return eval(new_str)
    return eval(relation)
    

print(is_it_true("2=2"))
print(is_it_true("8<7"))
print(is_it_true("5=13"))
print(is_it_true("15>4"))