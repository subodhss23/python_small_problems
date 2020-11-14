'''Create a function to convert a list of percentage to their decimal equivalents'''

def convert_to_decimal(lst):
    new_lst = []
    for i in lst:
        new_lst.append(float(i.strip('%'))/100)
    return new_lst

print(convert_to_decimal(["1%", "2%", "3%"]))
print(convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]))