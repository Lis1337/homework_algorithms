#with open('input.txt') as f:
    #k = int(f.readline())
    #n = int(f.readline())
    #asd = [int(x) for x in f.readline().split()]

k = 4
n = 7
coins = [4,3,2,3,5,2,1] #20        5 4 3 3 2 2 1 

res = {}
cur = 0




def funcc(k, n, coins, cur):
    coins.sort(reverse=True)
    s = sum(coins)
    target = s // k
    zxc = s % k

    if n < k or zxc != 0 or coins[cur] > zxc2:
        return False
    
    res[cur] = coins[cur]
