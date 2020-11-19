''' Create a function that reutrns the majority vote in a list. A majority vote is an element that 
    occurs > N/2 times in a list(where N is the length of the list).'''

def majority_vote(lst):
    counter = 0
    for i in lst:
        counter = lst.count(i)
        if counter > len(lst)/2:
            return i
    return None

print(majority_vote(["A", "A", "B"]))
print(majority_vote(["A", "A", "A", "B", "C", "A"]))
print(majority_vote(["A", "B", "B", "A", "C", "C"]))
print(majority_vote(["A", "B", "B", "B", "A", "A"]))