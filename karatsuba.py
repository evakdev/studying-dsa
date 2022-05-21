# Karatsuba algorithm is a way to multiply two big numbers in a way different from what we learned in third grade.
# Here we work with two numbers with same amount of digits. But this can be modified to work with different sizes.


import math


def karatsuba(x, y):
    # Base Case
    if x < 10 or y < 10:
        return x * y
    # get number of digits in each number, and find out where to divide the numbers.
    digit_num = max(math.ceil(math.log10(x)), math.ceil(math.log10(y)))
    divider = digit_num // 2
    divider += 1 if digit_num % 2 == 1 else +0

    # Divide numbers to two parts
    a, b = x // (10**divider), x % (10**divider)
    c, d = y // (10**divider), y % (10**divider)

    # Formula: (10**(2*divider)*ac) + (10**divider*((a+b)*(c+d) - ac - bd)) + bd
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ab_cd = ((a + b) * (c + d)) - ac - bd

    result = (10 ** (2 * divider)) * ac + (10**divider) * ab_cd + bd
    return result


def test_karatsuba():
    start, finish = 300, 600
    total_cases = finish - start
    correct = 0

    for i in range(start, finish):
        a = karatsuba(i, i + 1000)
        b = i * (i + 1000)
        if a == b:
            correct += 1
    print(
        f"Total Cases: {total_cases}\nCorrect Results:{correct} ({(correct/total_cases)*100}%)"
    )


test_karatsuba()
