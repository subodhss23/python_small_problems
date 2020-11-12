''' Given a dictionary of people and their ages, return how old the people
    would be after n years have passed. Use the absolute value of n.'''

def after_n_years(names, n):
    for key in names:
        names[key] = (names[key] + abs(n))
    return names

print(after_n_years({
  "Joel" : 32,
  "Fred" : 44,
  "Reginald" : 65,
  "Susan" : 33,
  "Julian" : 13
}, 1))

# print(after_n_years({
#   "Baby" : 2,
#   "Child" : 8,
#   "Teenager" : 15,
#   "Adult" : 25,
#   "Elderly" : 71
# }, 19))

# print(after_n_years({
#   "Genie" : 1000,
#   "Joe" : 40
# }, 5))