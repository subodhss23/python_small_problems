''' Create a function that takes a word and extends all vowels by a number num.'''

def extend_vowels(word, num):
	vols = 'aeiouAEIOU'
	new = ''
	if num < 0 or type(num) == float:
		return 'invalid'
	elif num == 0:
		return word
	else:
		for char in word:
			if char not in vols:
				new = new + char
			else:
				new = new + char + (char * num)
		return new

print(extend_vowels("Hello", 5))
print(extend_vowels("Edabit", 3))
print(extend_vowels("Extend", 0))
print(extend_vowels("Vowel", 0.5))