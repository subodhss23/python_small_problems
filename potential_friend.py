''' Given two sets of two people's different interests, return whether
    both people have at least two things in common or have exact interest.
    Return True if there's a potential friend!'''

def is_potential_friend(set1, set2):
    z = set1.intersection(set2)
    return len(z) >= 2 or set1 == set2

print(is_potential_friend(  {"sports", "music", "chess"},
                            {"coding", "music", "netflix", "chess"}))


print(is_potential_friend(
  {"cycling", "technology", "drawing"},
  {"dancing", "drawing"}
))

print(is_potential_friend(
  {"history"},
  {"history"}
))