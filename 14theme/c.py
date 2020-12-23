#n = 14
#asd = [5,3,7,2,8,26,-12,-30,-10,27,13,-20,-30,18]

#n = 15
#asd = [5,3,7,2,8,5,20,-19,-17,22,19,-16,6,11,-1]

with open('input.txt') as f:
    n = int(f.readline())
    asd = [int(x) for x in f.readline().split()]

def qsort(asd):
    if len(asd) < 2:
        return asd

    else:
        pivot = asd[0]
        less = [i for i in asd[1:] if i <= pivot]
        greater = [i for i in asd[1:] if i > pivot]
        return qsort(less) + [pivot] + qsort(greater)

print (*qsort(asd))
