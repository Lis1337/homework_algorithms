def split_number(num, max_len):  #id_41053260
    num = str(num)
    if len(num) < max_len:
        num = (max_len - len(num)) * '0' + num
    return list(num)
    

def sort_number(max_len, rang, array):
    for i in range(max_len - 1, -1, -1):
        temp = [[] for _ in range(rang)]
        for num in array:
            temp[int(num[i])].append(num)
            array = []
        for k in range(rang):
            array = array + temp[k]
    return array
    

if __name__ == '__main__':
    n = int(input())
    array = [int(x) for x in input().split()]
    max_len = len(str(max(array)))
    rang = 10
    array = [split_number(num, max_len) for num in array]
    array = [int(''.join(num)) for num in sort_number(max_len, rang, array)]
    print(*array)
