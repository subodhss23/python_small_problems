'''Given a dictionary of some items with star ratings and a specified star rating, return a new dictionary
    of items which match the specified star rating. Return "No result found" if no item match the start
    rating given. '''


def filter_by_rating(d, rating):
    new_obj = {}
    for i, j in d.items():
        if rating == j:
            new_obj[i] = j
    if new_obj == {}:
        return 'No results found'
    return new_obj



print(filter_by_rating({
  "Luxury Chocolates" : "*****",
  "Tasty Chocolates" : "****",
  "Aunty May Chocolates" : "*****",
  "Generic Chocolates" : "***"
}, "*****"))

# print(filter_by_rating({
#   "Continental Hotel" : "****",
#   "Big Street Hotel" : "**",
#   "Corner Hotel" : "**",
#   "Trashviews Hotel" : "*",
#   "Hazbins" : "*****"
# }, "*"))

# print(filter_by_rating({
#   "Solo Restaurant" : "***",
#   "Finest Dinings" : "*****",
#   "Burger Stand" : "***"
# }, "****"))