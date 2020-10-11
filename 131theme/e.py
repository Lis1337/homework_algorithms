with open('input.txt') as f:
    n = int(f.readline())

def fact(n):
    if n == 1 or n == 1:
        return 1
    return n * fact(n-1)

print(fact(n))