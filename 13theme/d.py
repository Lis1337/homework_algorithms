v = int(input())
n = int(input())
items = []
for i in range(n):
    items.append([int(x) for x in input().split()])


def solution(items, max_v):
    for i in range(0, len(items)):
        items[i].append(i)
    items.sort(key=lambda x: (x[0], -x[1]), reverse=True)

    v = 0
    result = []
    for i in items:
        if v <= max_v:
            if v + i[1] <= max_v:
                result.append(i[2])
                v += i[1]
            else:
                continue
    result.sort()
    print(' '.join(map(str, result)))

solution(items, v)