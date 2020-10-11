with open('input.txt') as f:
    n = int(f.readline())

asd = {
    0: 1,
    1: 1
}

def f(n):
    if n in asd:
        return asd[n]
    asd[n] = f(n-1) + f(n-2)
    return asd[n]

print(f(n))
