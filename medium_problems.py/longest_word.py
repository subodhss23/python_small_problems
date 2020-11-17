''' Write a function that finds the longest word in a sentence. If two
    of more words are found, return the first longest word. Characters such
    as apostophe, comma, period(and the like) count as part of the word.'''

# def longest_word(s):
#     new_lst = s.split(' ')
#     return max(new_lst, key=len)

def longest_word(s):
    word_lst = s.split(' ')
    result = ''
    for word in word_lst:
        if len(word) > len(result):
            result = word
    return result

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))