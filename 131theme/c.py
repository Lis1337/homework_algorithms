with open('input.txt') as f:
    n = int(f.readline())


asd = [0,1]
for i in range(28):
    asd.append(int(asd[-1]+int(asd[-2])))

print(asd[n+1])