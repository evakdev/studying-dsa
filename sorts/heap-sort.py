def sift_down(arr, ind):
    c1, c2 = (2 * ind) + 1, (2 * ind) + 2
    child = None
    if c1 >= len(arr):
        # We're already at leaf
        return arr
    if c1 >= len(arr) - 1:
        # Only one child exists
        child = c1
    else:
        # Both children exist, so we choose the bigger one
        max_num = max(arr[c1], arr[c2])
        child = c1 if max_num == arr[c1] else c2
    if arr[child] < arr[ind]:
        return arr
    arr[ind], arr[child] = arr[child], arr[ind]
    return sift_down(arr, child)


def heapify(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        print(i)
        arr = sift_down(arr, i)
        print(arr)
    return arr


arr = [3, 5, 1, 9, 2, 0, 10]

b = heapify(arr)
print(b)
