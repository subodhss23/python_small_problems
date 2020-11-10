''' If string contains "anime", "meme", "vines", "roasts", "Danny DeVito"
    return "NO!" otherwise, return "Safe watching!" '''

def prevent_distractions(txt):
	lst = ['anime', 'meme', 'vine','roasts', 'Danny DeVito']
	for i in lst:
		if i in txt:
			return 'NO!'
	return 'Safe watching!'

print(prevent_distractions("vines that butter my eggroll"))
print(prevent_distractions("Hot pictures of Danny DeVito"))
print(prevent_distractions("How to ace BC Calculus in 5 Easy Steps"))
