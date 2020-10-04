n = int(input())
m = int(input())
​
matrix = []
​
for i in range(n):
	row = [int(el) for el in input().split(' ')]
	matrix.append(row)
​
def spiral(m, n, a):
	l = 0
	k = 0
	while k < m and l < n:
		for i in range(l, n):
			print(a[k][i])
		k += 1
		
		for i in range(k, m):
			print(a[i][n - 1])
		n -= 1
		
		if k < m:
			for i in range(n - 1, l -1, -1):
				print(a[m - 1][i])
			m -= 1
		if l < n:
			for i in range(m - 1, k - 1, -1):
				print(a[i][l])
			l += 1
spiral(n, m, matrix)