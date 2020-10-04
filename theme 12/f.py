a = int(input())
asd = input().split()

n = {}
for i in asd:
    if i in n.keys():
        n[i] += 1
    else:
        n[i] = 1

for x in n.items():
    if x[1] > 1:
        print (x[0])