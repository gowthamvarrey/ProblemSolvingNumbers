arr = list(map(int, input().split()))
n = int(input())


def rotate(arr, n):
    return arr[len(arr) - n:] + arr[:len(arr) - n]


print(rotate(arr, n))
