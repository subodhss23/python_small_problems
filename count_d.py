# count nubmer of d in a string

def count_d(sentence):
    new_sen = sentence.lower()
    counter = 0
    for i in new_sen:
        if i == 'd':
            counter += 1
    return counter

print(count_d("My friend Dylan got distracted at school"))
print(count_d("Debris was scattered all over the place."))
print(count_d("The rodents hibernated in their den."))