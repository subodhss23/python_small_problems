''' Given a dictionary containing the names and ages of a group of people, return
    the name of the oldest person.'''

# def oldest(people):
#     max_value = max(list(people.values()))
#     for name, age in people.items():
#         if age == max_value:
#             return name
    

def oldest(people):
    for k in people:
        if people[k] == max(people.values()):
            return k


print(oldest({
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}))

# print(oldest({
#   "Max": 9,
#   "Josh": 13,
#   "Sam": 48,
#   "Anne": 33
# }))