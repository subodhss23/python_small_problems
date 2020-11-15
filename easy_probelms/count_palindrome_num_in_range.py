''' Create a function that returns the nubmer of palindrome numbers in a specified
    range(inclusive).'''
    

def count_palindromes(num1, num2):
    count = 0
    for i in range(num1, num2+1):
        if len(str(i)) == 1:
            count+=1
        else:
            if str(i) == str(i)[::-1]:
                count+=1
    return count

print(count_palindromes(1, 10))
print(count_palindromes(555,556))
print(count_palindromes(878, 898))