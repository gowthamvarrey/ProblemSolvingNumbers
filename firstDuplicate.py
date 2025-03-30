arr = list(map(int, input().split()))


def firstdup(arr):
    visited = []
    for i in arr:
        if i in visited:
            return i
        visited = visited + [i]


print(firstdup(arr))
