''' Given a string and a style character, return the newly formatted string.
    Style characters are single letters that represent the differenet types
    of formatting. 
    
    For the purposes of this challenge, the style characters are as follows:

        "b" is for bold
        "i" is for italics
        "c" is for inline code
        "s" is for strikethrough
'''

def md_format(word, style):
    if style == 'b':
        return "**" + word +"**"
    elif style == 'i':
        return "_" + word + "_"
    elif style == 'c':
        return '`'+ word + "`"
    elif style == 's':
        return '~~'+ word + "~~"

print(md_format("Bold", "b"))
print(md_format("leaning text", "i"))
print(md_format("Edabit", "c"))
print(md_format("That's a strike!", "s"))