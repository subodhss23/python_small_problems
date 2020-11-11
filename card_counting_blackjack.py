''' In BlackJack, cards are counted with -1,0,1 values:
    - 2,3,4,5,6 are counted as +1
    - 7,8,9 are counted as 0
    - 10,J,Q,K,A are counted as -1

    Create a function that counts the number and returns it from the list of cards provied.'''

def count(lst):
    sum = 0
    for i in lst:
        if i in [2,3,4,5,6]:
            sum += 1
        elif i in [7,8,9]:
            sum += 0
        elif i in [10, 'J', 'Q', 'K', 'A']:
            sum -= 1
    return sum

print(count([5, 9, 10, 3, "J", "A", 4, 8, 5]) )
print(count(["A", "A", "K", "Q", "Q", "J"]))
print(count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]))