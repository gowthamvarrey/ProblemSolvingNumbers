arr = [1, 2, [3, 4, [5, 5, [7, 8]]]]
new_arr = []


def flatten(arr):
    global new_arr
    for i in range(len(arr)):
        if type(arr[i]) == int:
            new_arr = new_arr + [arr[i]]
        else:
            flatten(arr[i])
    return new_arr


print(flatten(arr))
