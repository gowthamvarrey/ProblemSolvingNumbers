arr = input().split()


def getFreq(s):
    freq = [0] * 26
    for i in s:
        freq[ord(i) - ord('a')] += 1
    return tuple(freq)


def anagramsGrp(arr):
    res = {}
    for i in arr:
        k = getFreq(i)
        if k not in res:
            res[k] = [i]
        else:
            res[k] = res[k] + [i]
    return res


[print(i) for i in anagramsGrp(arr).values()]
print(anagramsGrp(arr).items())
