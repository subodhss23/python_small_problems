''' Write a function that takes a credit card number and and only displays the
    last four characters. The rest of the card number must be replaced by ************.'''

def card_hide(card):
    len_of_astrik = len(card) - 4
    return '*' * len_of_astrik + card[-4:]


print(card_hide("1234123456785678"))
print(card_hide("8754456321113213"))
print(card_hide("35123413355523"))