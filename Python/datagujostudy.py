def asterisk(n):
	if n > 1:
		asterisk(n/2)
		asterisk(n/2)
	print("*", end = '')
		
n = 5
asterisk(n)