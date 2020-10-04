n = 'abcabcbb'

arr = []
arr2 = []
for i in range(n):
    arr2.append(input())

for z in arr2:
    if z not in arr:
        arr.append(z)

print(*arr, sep='\n')