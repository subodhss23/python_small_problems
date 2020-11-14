''' Write a function that returns the number of users in a chatroom based on the following rules:

    1. If there is no one, return "no one online".
    2. If there is 1 person, return "user1 online".
    3. If there are 2 people, return user1 and user2 online".
    4. If there are n>2 people, return the first two names and add "add n-2 more online".
'''


def chatroom_status(lst):
    if len(lst) == 0:
        return 'no one online'
    elif len(lst) == 1:
        return lst[0] + ' online'
    elif len(lst) == 2:
        return lst[0] + ' and ' + lst[1] + ' online'
    else:
        return lst[0] + ', ' + lst[1] + 'and ' + str(len(lst) - 2) + ' more online'


print(chatroom_status([]))
print(chatroom_status(["paRIE_to"]))
print(chatroom_status(["s234f", "mailbox2"]))
print(chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"]))