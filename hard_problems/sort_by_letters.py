''' Write a function that sorts each string in a list by the letter in alphabetic ascending order(a-z)'''

def sort_by_letter(lst):
    new_lst = []
    new_obj = {}
    list_two = []
    for i in lst:
        for j in i:
            if j.isalpha():
                new_obj[j] = i
    sorted_lst =  sorted(new_obj)
    for i in sorted_lst:
        list_two.append(new_obj[i])
    return list_two



print(sort_by_letter(["932c", "832u32", "2344b"]))
print(sort_by_letter(["99a", "78b", "c2345", "11d"]))
print(sort_by_letter(["572z", "5y5", "304q2"]))
print(sort_by_letter([]))