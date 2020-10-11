#with open('input.txt') as f:
    #k = int(f.readline())
    #n = int(f.readline())
    #asd = [int(x) for x in f.readline().split()]

k = 4
n = 7
asd = [4,3,2,3,5,2,1]

def coin_counter(asd):
    if sum(asd) % k != 0:
        return False
    if k == 1:
        return True
    z = sum(asd) / k
    




print(coin_counter(asd))