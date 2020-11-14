''' Write a function that removes all capitals letters from a sentence except
    the first letter, put quotation marks around the sentence and add", 
    whispered Edabit." at the end.
'''

def shhh(txt):
	return '"{}", whispered Edabit.'.format(txt.capitalize())

print(shhh("HI THERE!") )
print(shhh("tHaT'S Pretty awesOme") )
print(shhh(""))
