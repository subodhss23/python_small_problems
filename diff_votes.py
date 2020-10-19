# return the difference of upvotes and downvotes

def get_vote_count(votes):
    return votes['upvotes'] - votes['downvotes']

print(get_vote_count({'upvotes': 13, 'downvotes': 0}))
print(get_vote_count({'upvotes': 2, 'downvotes': 33}))
print(get_vote_count({'upvotes': 132, 'downvotes': 132}))