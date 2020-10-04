n = int(input())
m = int(input())

arr = []
for z in range(n):
    arr.append(input().split(maxsplit=m))


arr2 = []
for x in range(m):
	arr2.append([arr[t][x] for t in range(n)])
for h in arr2:
	print(' '.join(h))

#[['1', '2', '3'],
# ['0', '2', '6'],
# ['7', '4', '1'],
# ['2', '7', '0']]