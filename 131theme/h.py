#with open('input.txt') as f:
    #n = int(f.readline())
n = 3
s = 2*n
open = 0
close = 0


def func(cur, open, close, n):
    if len(cur) == 2 * n:
        print(cur)
        return

    if open < n:
        func(cur + '(', open + 1, close, n)

    if close < open:
        func(cur + ')', open, close + 1, n)

func('', close, open, n)