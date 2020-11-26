''' Create a function that returns True if two lines rhyme and False otherwise. For the purpose of this exercise,
    two lines rhyme if the last word from each sentence contains the same vowels.'''


def does_rhyme(txt1, txt2):
    one = (txt1.split(' ')[-1]).lower()
    two = (txt2.split(' ')[-1]).lower()
    vowel = 'aeiou'
    one_one = []
    two_two = []
    for i in one:
        if i in vowel:
            one_one.append(i)
    for i in two:
        if i in vowel:
            two_two.append(i)
    return one_one == two_two

print(does_rhyme("Sam I am!", "Green eggs and ham."))  
print(does_rhyme("Sam I am!", "Green eggs and HAM."))
print(does_rhyme("You are off to the races", "a splendid day."))
print(does_rhyme("and frequently do?", "you gotta move."))