''' Additional spaces have been added to a sentence. Return the correct 
    sentence by removing them. All words should be separated by one space, and
    there should ne no space at the begenning or end of the sentence. '''

def correct_spacing(sentence):
    new_lst = sentence.split()
    return ' '.join(new_lst)

print(correct_spacing("The film   starts       at      midnight. "))
print(correct_spacing("The     waves were crashing  on the     shore.   "))
print(correct_spacing(" Always look on    the bright   side of  life."))