row = int(input())
count = (row * (row + 1)) // 2
print(count)


def fibbi(count):
    arr = [0, 1]
    if count <= 2:
        return arr[:count]
    else:
        for i in range(count - 2):
            arr.append(arr[-1] + arr[-2])
        return arr


arr = fibbi(count)

for i in range(1, row + 1):
    pointer = i - 1
    incre = row - 1
    for j in range(1, i + 1):
        print(arr[pointer], end=" ")
        pointer += incre
        incre -= 1

    print()
