c = input()

def pod(string):
	maxlen = 0
	for i in range(len(string)):
		substring = string[i:]
		chars = set()
		for j, c in enumerate(substring):
			if c in chars:
				break
			else:
				chars.add(c)
		else:
			j += 1

		if j > maxlen:
			maxlen = j
	return maxlen
	
print(pod(c))