# ways to represent an infinite integer:
# num = float("inf") (negative: float("-inf"))
# import math.  num = math.inf


def selection_sort(ls):
    sorted_pointer = 0  # where to place next sorted item
    unsorted_pointer = 0  # start of unsorted list
    # both pointers will be equal at the beginning of each loop. but we cant use a single one because
    # it changes during the loop.
    length = len(ls)
    while (
        sorted_pointer < length
    ):  # ---> this condition also takes care of len=0 situation
        # find the smallest in the unsorted
        min_num = float("inf")  # represents an infinite integer
        min_ind = length
        # we have to go through the whole for loop for every single item, cannot break.
        for i in range(unsorted_pointer, length):
            if ls[i] < min_num:
                min_num = ls[i]
                min_ind = i

        ls[min_ind], ls[sorted_pointer] = ls[sorted_pointer], ls[min_ind]
        sorted_pointer += 1
        unsorted_pointer += 1
    return ls


ls = [1, 10, 10, 0]
print(selection_sort(ls))


# General Idea:
# Iterate array to find the smallest item. remove it from array and add it to sorted list. rinse and repeat.
# in-place: find smallest, the swap it with index 0. then find the next smallest, swap it with index 1, etc.
# here too, [:i] is sorted, [i:] is unsorted


# Order:
# for array and linkedlist: O(n^2)
# Why?
# if not in place, removing takes shifting too.
# if in place:
# you need a linear search to find the smallest item.(n) then you need to find its new place (n)
# its true that it takes -1 time to find smallest after each iteration....so why n^2?
# because if you sum all that it would be (start+last)*(count/2) -> (n+1)*(n/2)==(n+n^2)/2 ==>(n^2)/2
# which doesnt differ much from n^2

# doesnt matter what your input is, or your structure. it will always be n^2, EVEN IN BEST CASE


# Pros
# If s is array, its in-place.
# if you have an array that you think is sorted, but want to verify that it is,
# it can be much less.
# If array is almost sorted, it'll take much less time.
