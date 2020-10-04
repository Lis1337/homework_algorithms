q = int(input())
qwe = [input().split() for t in range(q)]


qwe.sort(key=lambda x: (float(x[1]), float(x[0])))
res = [qwe[0]]
i = 0
for z in range(1, q):
    begin_sec = float(qwe[z][0])
    end_first = float(res[i][1])
    if begin_sec >= end_first:
        res.append(qwe[z])
        i += 1

print(len(res))
for c in res:
    print(*c)