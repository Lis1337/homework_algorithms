def greater_num(num):    #id_40973454
    return (num * 4)[:4]


if __name__ == '__main__':
    quantity = int(input())
    array = input().split()
    array.sort(key=greater_num, reverse=True)
    print(''.join(array))
