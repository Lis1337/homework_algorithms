with open('input.txt') as f:
    n = int(f.readline())

def fib(n):
    if n in (0, 1):
        return 1
    return fib(n-1) + fib(n-2)

print(fib(n))