def binary_search(array, item, left, right):    #id 39452523
    if right >= left:
        mid = left + (right - left) // 2
        if array[mid] == item:
            return mid
        if array[mid] < array[right]:
            if array[mid] < item <= array[right]:
                tmp = [mid + 1, right]
            else:
                tmp = [left, mid - 1]
        else:
            if array[left] <= item < array[mid]:
                tmp = [left, mid - 1]
            else:
                tmp = [mid + 1, right]
        return binary_search(array, item, *tmp)
    else:
        return -1

if __name__ == "__main__":
    list_length = int(input())
    seek_elem = int(input())
    my_array = [int(x) for x in input().split()]
    print(binary_search(my_array, seek_elem, 0, list_length - 1))
