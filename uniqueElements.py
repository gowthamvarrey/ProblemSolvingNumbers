arr = list(map(int, input().split()))


def getUnique(arr):
    res = {}
    for i in arr:
        if i not in res:
            count = 0
            for j in arr:
                if i == j : count += 1
            res[i] = count
    print(res)
    l = []
    for key, value in res.items():
        if value == 1:
            l.append(key)
    return l


x = getUnique(arr)
print(x)

