def radix_sort(array):
    max_len = len(max(array, key=int))

    def sorting(item):
        item = "0" * (max_len - len(item)) + item
        return item[i]


    for i in range(max_len-1, -1, -1):
        array.sort(key=sorting)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        numbers = f.readline().split() if n else []

    radix_sort(numbers)

    with open("output.txt", "w") as f:
        f.write(" ".join(numbers))
