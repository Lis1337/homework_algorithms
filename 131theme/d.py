with open('input.txt') as f:
    n = int(f.readline())

M = {
    0: 1,
    1: 1,
    2: 2,
    3: 3
}


def fib(n):
    if n in M:
        return M[n]
    M[n] = fib(n-1) + fib(n-2)
    return M[n]

print(list(str(fib(n)))[-1])