with open('input.txt') as f:
    m = int(f.readline())
    n = int(f.readline())
    coins = [int(x) for x in f.readline().split()]


def func(m, coins):
    if m == 0:
        return 1

    if m < 0 or not coins:
        return 0
    
    return func(m - coins[0], coins) + func(m, coins[1:])

print(func(m, coins))