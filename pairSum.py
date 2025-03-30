arr = list(map(int, input().split()))
target = int(input())

def pairSum(arr, target):
    res = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                res = res + [[arr[i], arr[j]]]
    return res


print(pairSum(arr, target))
