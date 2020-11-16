'''Jay and Silent Bob have beern given a fraction of an ounce but they only
    understand grams. Convert a fraction passed as a sting to grams with up to
    two decimal places. An ounce weighs 28 grams.'''

def jay_and_bob(txt):
    ounce = 28
    if txt == "half":
        return str(round(ounce / 2)) + ' grams'
    elif txt == "quarter":
        return str(round(ounce / 4)) + ' grams'
    elif txt == 'eighth':
        return str(ounce / 8) + ' grams'
    elif txt == 'sixteenth':
        return str(ounce/16) + ' grams'

print(jay_and_bob("half"))
print(jay_and_bob("quarter"))
print(jay_and_bob("eighth"))
print(jay_and_bob("sixteenth"))