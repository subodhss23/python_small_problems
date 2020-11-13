''' A group of friends have decided to start a secret society. The name will
    be the first letter of each of their names, sorted in alphabetical order.

    Create a function that takes in a list of names and returns the name of the 
    secret society.'''

def society_name(lst):
    new_str = ''
    for i in lst:
        new_str+= i[0]
    sorted_lst = sorted(new_str)
    return ('').join(sorted_lst)

print(society_name(["Adam", "Sarah", "Malcolm"]))
print(society_name(["Harry", "Newt", "Luna", "Cho"]))
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))