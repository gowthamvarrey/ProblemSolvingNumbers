arr = list(map(int, input().split()))


def reverseArray(arr):
    x = []
    for i in range(len(arr)-1,-1,-1):
        x = x + [arr[i]]
    return x


print(reverseArray(arr))


