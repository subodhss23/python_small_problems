''' Create a function which takes in a sentence txt and a string of character
    chars and return the sentence but with all specified characters removed. '''


def strip_sentence(txt, chars):
    new_str = ""
    for i in txt:
        if i not in chars:
            new_str+=i
    return new_str


print(strip_sentence("the quick brown fox jumps over the lazy dog", "aeiou"))
print(strip_sentence("the hissing snakes sinisterly slither across the rustling leaves", "s"))
print(strip_sentence("gone, reduced to atoms", "go, muscat nerd"))