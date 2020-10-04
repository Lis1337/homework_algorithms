with open('input.txt') as f:
    n = int(f.readline())

def fact(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(n))