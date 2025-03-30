arr = list(map(int, input().split()))


def moveToEnd(arr):
    i = 0
    count = 0
    while i < len(arr):
        if arr[i] == 0:
            count += 1
            for j in range(i, len(arr) - 1):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if arr[i] != 0 or i > len(arr) - count:
            i += 1
    return arr


print(moveToEnd(arr))
