import collections

ids = input().split()
k = int(input())

for i in collections.Counter(ids).most_common(k):
    print(i[0], end=' ')