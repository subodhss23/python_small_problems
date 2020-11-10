def pH_name(pH):
	if pH > 7 and pH < 14.0:
		return 'alkaline'
	elif pH < 7 and pH > 0:
		return 'acidic'
	elif pH >= 7.0 and pH <= 7.9:
		return 'neutral'
	elif pH < 0.0 or pH > 14.0:
		return 'invalid'

print(pH_name(7.2))