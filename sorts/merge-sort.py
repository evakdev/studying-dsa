def merge_sort(ls):
    length = len(ls) - 1
    # Base Case
    if len(ls) <= 1:
        return ls
    l, r = 0, length - 1

    # Finding mid index. this will be the exclusive limit of left half, and inclusive limit of right half.
    mid = (r - l) // 2 + 1
    # Notes on finding mid
    # if mid = (l-r)//2, then for a list of len 2 mid it will be (1-0)//2 = 0. which will make list: [],[a,b]
    # if so, we would get stuck in the loop since the two-item list is never getting divided and merged.
    # so, we add 1 ----> if len(2): mid = 0 + 1 = 1    ---> lists: [a],[b]

    # one could also use len(ls)//2 for mid. it would divide an odd list a bit different but
    # that doesnt make an issue for the loop, and certainly not for cases of len=2
    # if we hadn't had our base case as len<=1, then len of 1 would become an issue. but we handle that, so all is good.

    left = merge_sort(ls[:mid])
    right = merge_sort(ls[mid:])
    final = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        # notes on why i've included equality here instead of adding both nums in case of equality:
        # if I added both, there could be a case where both i, j would equal their lists' len.
        # Then, my if elif conds after loop would throw an error, because i/j are exceeding list index.
        #  (if i = len(left), then left[i:] is wrong)
        # so instead of fixing that, I just remove that part. it would only save a small number of checks for me,
        # and now I'm writing less code!

        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        elif right[j] < left[i]:
            final.append(right[j])
            j += 1

    # why not use append here rather than summing? because append takes one single item, not list.
    # and *right doesnt work either.
    if i == len(left):
        final += right[j:]
    elif j == len(right):
        final += left[i:]
    return final


ls = [0, 0, 9, 10, 1]
print(merge_sort(ls))


# General Idea:
# we will use the fact that we can merge two sorted lists together in linear time (similiar to set union, except
# we dont remove duplicates here)
# Divide and conquer. Recursively cut lists in half, until you get to lists of one item. then sort the smallest
# lists. next, merge the two half-lists in sorted order by comparing l1[i] to l2[i] and getting the bigger one
# in the sorted list. once one of the lists is finished, join the other one to the sorted list since all of its
# items are gonna be bigger than last sorted item.
# can be faster for linkedlist than quicksort
# Order:
# O(nlogn)
# Why?
# the number of times the recursion runs is gonna be 1+logn, so logn. (e.g if 4 items -->2 + 1)
# at each step (when combining the parts) we will be sorting all of the items we have, so n
# ---> nlogn

# doesnt matter what your input is, or your structure. it will always be n^2, EVEN IN BEST CASE


# Pros
# natural choice for linked list, a little clumsy for arrays.
# will not be in-place for the array, so you need double the memory since you need one extra array
