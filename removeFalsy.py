arr = input().split()


def removeFalsy(arr):
    falseValues = ['False', '0', 'None']
    res = []
    for i in arr:
        if i not in falseValues:
            res = res + [i]
    return res


print(removeFalsy(arr))
