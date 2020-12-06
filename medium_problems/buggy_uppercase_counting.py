''' In the code tab is a function which is meant to return how many uppercase 
    letters there are in a list of various words. Fix the code so it works normally.'''

def count_uppercase(lst):
    counter = 0
    for word in lst:
        for letter in word:
            if letter.isupper():
                counter+=1
    return counter
        

print(count_uppercase(["SOLO", "hello", "Tea", "wHat"]))