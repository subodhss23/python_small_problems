''' Two sisters are eating chocolate, whose pieces are represented as subarrays of [l x w].

    Write a function that returns True if the total area of chocolate is the same of each sister.'''


def test_fairness(agatha, bertha):
    one = 0
    two = 0
    for i in range(len(agatha)):
        one+=helper(agatha[i])
    for i in range(len(bertha)):
        two+=helper(bertha[i])
    return one == two

def helper(lst):
    return lst[0] * lst[1]


print(test_fairness([[1, 2], [2, 1]], [[2, 2]]))
print(test_fairness([[1, 2], [2, 1]], [[2, 2], [4, 4]]))
print(test_fairness([[2, 2], [2, 2], [2, 2], [2, 2]], [[4, 4]]))
print(test_fairness([[1, 5], [6, 3], [1, 1]], [[7, 1], [2, 2], [1, 1]]))
