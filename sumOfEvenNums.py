arr = list(map(int, input().split()))


def sumOfEven(arr):
    sum = 0
    for i in arr:
        if i % 2 == 0:
            sum += i
    return sum


print(sumOfEven(arr))
