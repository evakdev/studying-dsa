### Insertion Sort

ls = [31, 21, 41, 59, 26, 58]

print("initial list:", ls)
for key_ind in range(1, len(ls)):  # 1
    key = ls[key_ind]  # 21
    checking_num_ind = key_ind - 1  # 0
    print("current key:", key)

    while checking_num_ind >= 0 and key < ls[checking_num_ind]:  # True True
        ls[checking_num_ind + 1] = ls[checking_num_ind]  # ls=[31,31,41,...]
        checking_num_ind -= 1  # -1
        print("in-checking:", ls)
    ls[checking_num_ind + 1] = key
    print("after for loop:", ls)

print("final sorted list:", ls)
