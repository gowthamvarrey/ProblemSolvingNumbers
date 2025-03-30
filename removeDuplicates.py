arr = list(map(int, input().split()))


def removeDups(arr):
    result_array = []
    for i in arr:
        if i not in result_array:
            result_array = result_array + [i]
    return result_array


print(removeDups(arr))
