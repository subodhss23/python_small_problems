''' Given a list of prices "prices" and a  "supposed" total t, return True if there
    is a hidden fee added to the total(i.e. the total is greater than the sum of prices),
    otherwise return False.'''

def has_hidden_fee(prices, t):
    sum = 0
    new_lst = []
    for i in prices:
        new_lst.append(i.strip('$'))
    for i in new_lst:
        sum+=int(i)
    return sum < int(t.strip('$'))

print(has_hidden_fee(["$2", "$4", "$1", "$8"], "$15"))
print(has_hidden_fee(["$1", "$2", "$3"], "$6"))
print(has_hidden_fee(["$1"], "$4"))