arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


def intersected(arr1, arr2):
    res = []
    for i in arr1:
        if i in arr2:
            res.append(i)
    return res


print(intersected(arr1, arr2))
