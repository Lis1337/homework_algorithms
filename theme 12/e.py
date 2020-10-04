x = int(input())
z = list(str(bin(x)))
asd = z[2:len(z)]
zxc = int(''.join(map(str, asd)))

print(zxc)