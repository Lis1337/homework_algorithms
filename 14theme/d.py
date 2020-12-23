length1 = 3
length2 = 8

l1 = [4,9,5]
l2 = [9,4,9,8,4]

res = []

#with open('input.txt') as f:
    #length1 = int(f.readline())
    #length2 = int(f.readline())
    #l1 = [int(x) for x in f.readline().split()]
    #l2 = [int(x) for x in f.readline().split()]


def roach(l1,l2):
    res = []
    for i in l1:
        if i in l2:
            res.append(i)
        