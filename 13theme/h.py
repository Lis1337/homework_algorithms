n = int(input())
asd = input().split()

k = 1
count = 0
while k < len(asd):
    if int(asd[k]) > int(asd[k-1]):
        count += 1
    k += 1

print(count)