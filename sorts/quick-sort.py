import random


def quicksort(ls):
    def get_pivot_index(ls):
        length = len(ls)
        if length <= 10:
            return random.randrange(0, length)
        rands = []

        while len(rands) < 3:
            rands.append(random.randrange(0, length))

        return sorted(rands)[1]

    length = len(ls)
    if length <= 1:
        return ls

    pivot_ind = get_pivot_index(ls)
    pivot = ls[pivot_ind]
    print(f"{length=},{pivot=}")
    left, right = [], []
    for i in range(length):
        if i == pivot_ind:
            continue
        if ls[i] <= pivot:
            left.append(ls[i])
        else:
            right.append(ls[i])
    print(left, right)
    return quicksort(left) + [pivot] + quicksort(right)


ls = [random.randrange(-100, 100) for i in range(50)]
print(quicksort(ls))

# Fastest comparison-based sort known for arrays
# worst-case tetha n2, but virtually always O(nlogn) in practice, but in average!
# if we have a big len, like more than 10, it can be faster to get the median of 3 randoms instead of 1
