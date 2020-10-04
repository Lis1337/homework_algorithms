qwe = str(input())
qwe2 = str(input())

q = int(qwe, 2)
q2 = int(qwe2, 2)

asd = q + q2

zxc = list(str(bin(asd)))
zxc2= zxc[2:len(zxc)]

print (int(''.join(map(str, zxc2))))