arr = list(map(int,input().split()))

def longestSeq(arr):
    seq = 0
    count = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            count += 1
        else:
            if(seq < count):
                seq = count
            count=0
    return seq

print(longestSeq(arr))
