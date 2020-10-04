asd = ['5','3','2','4','1']
x = 0

for i in asd:
    if type(i) == int:
        if int(i) > x:
            x = i
print(x)