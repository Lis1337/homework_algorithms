def radix_sort(array):  #id__41056603

    def split_number(num, max_len):
        num = str(num)
        if len(num) < max_len:
            num = (max_len - len(num)) * '0' + num
        return list(num)


    def sorting(max_len, rang, array):
        for i in range(max_len - 1, -1, -1):
            temp = [[] for x in range(rang)]
            for num in array:
                temp[int(num[i])].append(num)
                array = []
            for k in range(rang):
                array = array + temp[k]
        return array 


    max_len = len(str(max(array, key=int)))
    rang = 10
    array = [split_number(num, max_len) for num in array]
    array = [int(''.join(num)) for num in sorting(max_len, rang, array)]
    return array


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        array = f.readline().split() if n else []
    print(*radix_sort(array))
