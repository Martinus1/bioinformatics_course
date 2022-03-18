genome = "GCATACACTTCCCAGTAGGTACTG"
skew = []
skew_value = 0

for n in genome:
	if n == 'G':
		skew_value += 1
		skew.append(skew_value)
	elif n == 'C':
		skew_value -= 1
		skew.append(skew_value)

print(skew)
