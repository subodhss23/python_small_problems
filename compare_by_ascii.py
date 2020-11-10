'''Create a function that compares two words based on the sum of their ASCII codes
    and returns the word with the smaller ASCII sum. '''

def ascii_sort(lst):
    one, two = lst  #destruction baabbbyyy
    one_lst = list(one)
    two_lst = list(two)
    sum_one = 0
    sum_two = 0
    for i in one_lst:
        sum_one+=ord(i)
    for j in two_lst:
        sum_two+=ord(j)
    if sum_one > sum_two:
        return two
    elif sum_one < sum_two:
        return one
        
print(ascii_sort(["hey", "man"]) )
print(ascii_sort(["majorly", "then"]))
print(ascii_sort(["victory", "careless"]))