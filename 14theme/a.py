#n = 14
#asd = [5, 3, 7, 2, 8, 26, -12, -30, -10, 27, 13, -20, -30, 18]


with open('input.txt') as f:
    n = int(f.readline())
    asd = [int(x) for x in f.readline().split()]

def sorting(asd):
    for i in range(len(asd)-1):
        replace = False
        min_el = asd[i]
        for x in range(i, len(asd)):
            if asd[x] < min_el:
                replace = True
                min_el = asd[x]
                min_pos = x
        if replace:
            tmp = asd[i]
            asd[i] = min_el
            asd[min_pos] = tmp
    return asd

print(*(sorting(asd)))
