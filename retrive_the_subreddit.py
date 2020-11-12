#Create a function to extract the name of the subreddit from its URL.

def sub_reddit(link):
    new_lst = link.split('/')
    return new_lst[4]

print(sub_reddit("https://www.reddit.com/r/funny/"))
print(sub_reddit("https://www.reddit.com/r/relationships/") )
print(sub_reddit("https://www.reddit.com/r/mildlyinteresting/"))