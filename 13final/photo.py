def foto_copy(memory_data, data_centers):   #id 39261564
    copy = 0
    memory_data.sort()
    list_variable = []
    while len(memory_data) > 1:
        if memory_data[-1] > 0 and memory_data[-2] > 0:
            memory_data[-1] -= 1
            memory_data[-2] -= 1
            copy += 1
            memory_data.sort()
        while memory_data and memory_data[0] == 0:
            memory_data.pop(0)
    return copy

if __name__ == "__main__":
    data_centers = int(input())
    memory_data = [int(x) for x in input().split()]
    print(foto_copy(memory_data, data_centers))
