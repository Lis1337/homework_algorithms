a = int(input())
b = ''
while a > 0:
    b = str(a % 2) + b
    a = a // 2

c = list(str(b))

d = 0
for i in c:
    if int(i) == 1:
        d += 1

print (d)