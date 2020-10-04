with open('input.txt') as f:
    n = int(f.readline())

i = n
while i > 1:
    i -= 1
    n = n * i
print (n)