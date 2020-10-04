n = int(input())
asd = input().split()


summ = 0
i = 0
while i < int(len(asd))-1:
    if int(asd[i]) < int(asd[i+1]):
        summ = summ - int(asd[i]) + int(asd[i+1])
    i += 1

print(summ)