def interview(lst, tot):
	very_easy = 5
	easy = 10
	medium = 15
	hard = 20
	if len(lst) >= 8:
		if tot > 120 or lst[0] > 5 or lst[1] > 5 or lst[2] > 10 or lst[3] > 10 or lst[4] > 15 or lst[5] > 15 or lst[6] > 20 or lst[7] > 20:
			return 'disqualified'
		return 'qualified'
	elif len(lst) < 8:
		return 'disqualified'


print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))