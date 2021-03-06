n = 23

with open('input.txt') as f:
    n = int(f.readline())

M = {
    0: 1,
    1: 1
}


def fib(n):
    if n in M:
        return M[n] % 10
    M[n] = (fib(n-1))%10 + (fib(n-2))%10
    return M[n]

print(fib(n)%10)