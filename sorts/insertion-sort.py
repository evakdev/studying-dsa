"""def insertion_sort(ls: list):
    # in-place (default)
    if len(ls) <= 1:
        return ls
    p1 = 0  # last sorted item
    p2 = p1  # to traverse sorted list
    p3 = p1 + 1  # to traverse unsorted list

    while p3 < len(ls):
        # find place in sorted, starting from the end of sorted list, linear search (o(n))
        # if item is bigger than sorted item, shift sorted item forward
        # in each turn, move p2 pointer back by one
        # if item gets smaller than sorted item or we reach the end of list,
        # put item at p2+1 (so if list was ended p2 would be -1, which makes p2+1 first of the list)
        p2 = p1
        num = ls[p3]
        while p2 >= 0:
            if ls[p2] < num:
                break
            else:
                ls[p2 + 1] = ls[p2]
            p2 -= 1
        ls[p2 + 1] = num
        p1 += 1
        p3 += 1
    return ls"""


def insertion_sort(ls: list):
    # in-place (default)
    if len(ls) <= 1:
        return ls
    p1 = 0 + 1  # first unsorted item last sorted item
    p2 = p1 - 1  # to traverse sorted list
    p3 = p1  # to traverse unsorted list

    while p3 < len(ls):
        # find place in sorted, starting from the end of sorted list, linear search (o(n))
        # if item is bigger than sorted item, shift sorted item forward
        # in each turn, move p2 pointer back by one
        # if item gets smaller than sorted item or we reach the end of list,
        # put item at p2+1 (so if list was ended p2 would be -1, which makes p2+1 first of the list)

        num = ls[p3]
        while p2 > 0:
            if ls[p2 - 1] < num:
                break
            else:
                ls[p2] = ls[p2 - 1]
            p2 -= 1
        ls[p2] = num
        p1 += 1
        p3 += 1
    return ls


print(insertion_sort([3, 9, 0, 1, 2]))
# General Idea:
# starting from the beginning, take each item and find its place in the sorted list. put it there.
# In-place:
# divide array into two parts: [:1] is sorted, [1:] is unsorted. for each item in unsorted,
# find its place in sorted. then move every item after by one place.

# Order:
# for array and linkedlist: O(n^2)
# Why?
# in linked-list:
# You still have to traverse the list. find the new place among the unsorted.
# in array:
# If two arrays, then you still have to find its place in new list[which increases by one
# each time, but if you sum all that it would be (start+last)*(count/2) -> (n+1)*(n/2)==(n+n^2)/2 ==>(n^2)/2
# which doesnt differ much from n^2
# you can use binary search to make it nlogn, but if inplace it will still be n^2 because
# you have to shift each of sorted items by one in each placement

# for a BALANCED search tree it can be O(nlogn)

# Pros
# If s is array, its in-place.
# if you have an array that you think is sorted, but want to verify that it is,
# it can be much less.
# If array is almost sorted, it'll take much less time. especially if you check the sorted list
# starting from its end
