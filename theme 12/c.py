x = int(input())
asd = input().split()
k = int(input())

zxc = int(''.join(map(str, asd)))

res = list(str(k+zxc))

print(*res)