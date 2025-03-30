arr = list(map(int, input().split()))


def findMissing(arr):
    for i in range(len(arr)-1):
        if arr[i] + 1 != arr[i + 1]:
            return arr[i] + 1
    return -1


print("Missing number in the sequences is", findMissing(arr))
