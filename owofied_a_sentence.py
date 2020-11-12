''' Create a function that takes a sentence and turns every 'i' into 'wi' and 'e'
    into 'we', and add 'owo' at the end.'''

def owofied(sentence):
    new_sentence = ''
    for i in sentence:
        if i == 'i':
            new_sentence += 'wi'
        elif i == 'e':
            new_sentence += 'we'
        else:
            new_sentence+=i
    return new_sentence + ' owo'

print(owofied("I'm gonna ride 'til I can't no more"))