''' The insurance guy calls again. Apparently, they were informed by your spouse that some
    items were not stolen at all and you failed to mention this detail to them. This is
    a fraud attempt! You freeze and mumble something unintelligible. Find out what you said.

    Given a dictionary, return a string that concatenates all the values and adds the 2nd 
    key at the end. Make sure you keep an empty space between them but not at the beginning or
    end of the string. Look at the examples from the clearer picture. 

    Examples:

    { 1: "Mommy", 2: "please", 3: "help" } ➞ "Mommy please help please"

    { 1: "Me", 2: "innocent", 3: "is" } ➞ "Me innocent is innocent"

    { 1: "Must", 2: "lawyer", 3: "call" } ➞ "Must lawyer call lawyer"

    Notes:

    - The keys will always be 1: 2: 3: etc. in this order. Don't mistake keys with indexes.
    - I'm rating the challenge very easy because it can be hardcoded but try to do it dynamically,
    that is, if you receive a dictionary with 4 keys instead, your function should still work.'''


def say_what(obj):
    new_lst = []
    for i in range(1,len(obj)+1):
        new_lst.append(obj[i])
    new_lst.append(obj[2])
    return (' ').join(new_lst)

    # new_lst.append(obj[1])
    # new_lst.append(obj[2])
    # new_lst.append(obj[3])
    # new_lst.append(obj[2])
    # return new_lst

print(say_what({ 1: "Mommy", 2: "please", 3: "help" }))
# print(say_what({ 1: "Me", 2: "innocent", 3: "is" }))
# print(say_what({ 1: "Must", 2: "lawyer", 3: "call" }))