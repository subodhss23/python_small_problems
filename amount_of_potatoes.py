# create a function to return the amount of potatoes there are in a string.

# def potatoes(potato):
#    temp_lst = []
#    counter = 0
#    for i in potato:
#        if i == "p":
#            counter += 1
#            print("inside the counter")
#     print(counter)


def potatoes(potato):
    counter = 0
    for i in potato:
        if i == "p":
            counter += 1
    return counter

print(potatoes("potatopotatocherry"))
print(potatoes("potatopotatopotatoorange"))