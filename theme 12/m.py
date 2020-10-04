asd = str(input())

zxc = list(asd)

n = {}
for i in zxc:
    if i in n.keys():
        n[i] += 1
    else:
        n[i] = 1

d = []
for x in n.items():
    d.append(x[0]*x[1])

print (''.join(sorted(d)))