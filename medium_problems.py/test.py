def operation(a, b, op):
	if op == 'add':
		print('we in add')
		return str(int(a) + int(b))
	elif op == 'subtract':
		print('we in sub')
		return str(int(a) - int(b))
	elif op == 'multiply':
		print('we in mult')
		return str(int(a) * int(b))
	elif op == 'divide':
		if b == '0':
			return 'undefined'
		print('we in divide')
		return str(int(a) // int(b))