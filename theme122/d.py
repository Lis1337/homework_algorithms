
#qwe = [['1', '2', '3'], ['0', '2', '6'], ['7', '4', '1'], ['2', '7', '0']]


n = int(input())
m = int(input())
qwe = []
for z in range(n):
    qwe.append(input().split(maxsplit=m))    
q = int(input())
e = int(input())
       
def some_func3(qwe, q, e):
    res = []
    try:
        if q >= 1:
            res.append(int(qwe[q-1][e]))
        else:
            pass
    except: IndexError

    try:
        if e >= 1:
            res.append(int(qwe[q][e-1]))
        else:
            pass
    except: IndexError

    try: res.append(int(qwe[q+1][e]))
    except: IndexError

    try: res.append(int(qwe[q][e+1]))
    except: IndexError
    
    print(*(sorted(res)))

some_func3(qwe, q, e)

#[['1', '2', '3'], 
# ['0', '2', '6'], 
# ['7', '4', '1'], 
# ['2', '7', '0']] 



    #if q == 0 and e == 0:
        #res.append(qwe[q+1][e])
        #res.append(qwe[q][e+1])

    #elif q == qwe.index(qwe[-1]) and e == 0:
        #res.append(qwe[q-1][e])
        #res.append(qwe[q][e+1])

    #elif q == 0 and e == int(len(qwe[q]))-1:
        #res.append(qwe[q+1][e])
        #res.append(qwe[q][e-1])

    #elif q == qwe.index(qwe[-1]) and e == int(len(qwe[q]))-1:
        #res.append(qwe[q-1][e])
        #res.append(qwe[q][e-1])

    #else: