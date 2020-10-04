n = int(input())
l = list(map(int, input().split()))
k = set()
for i in range(1, n):
    k.add(i)
for index, v in enumerate(l):
    les = {index + j for j in range(1, v+1)}
    k -= les
print(k == set())