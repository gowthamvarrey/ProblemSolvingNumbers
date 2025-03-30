arr = list(map(int, input().split()))


def maxProduct(arr):
    maxp = float('-inf')
    for i in range(len(arr) - 1):
        product = arr[i] * arr[i + 1]
        if product > maxp:
            maxp = product
    return maxp


print(maxProduct(arr))
