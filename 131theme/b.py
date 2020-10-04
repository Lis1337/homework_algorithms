#with open('input.txt') as f:
    #n = int(f.readline())

def fib(n):
    if n in (0, 1):
        return 1
    elif n == 2:
        return 2
    return fib((n-1)+(n-2))

print(fib(int(input())))