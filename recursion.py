#!/usr/bin/env python
# -*- Coding: Utf-8 -*-

"""
Week 14 assignment: recursive functions
"""

def fibonacci(n):
    """
    Calculate nth number of Fibonacci sequence
    :param n: (Int) 0 <= n
    :return: (Int or False)
    """
    if isinstance(n, int) and n > 0:
        if n == 1 or n == 0:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return False


def gcd(num_a, num_b):
    """
    Find the greatest common divisor
    :param num_a: (Int) Dividend
    :param num_b: (Int) Divisor
    :return: (Int or False)
    """

    if num_b == 0 or num_a < num_b:
        return False
    div = num_a
    rem = num_a % num_b
    if rem == 0:
        return num_b
    else:
        return gcd(div, rem)


def strcomp(str1, str2):
    """
    Compare two strings
    :param str1:
    :param str2:
    :return:
    """
    # Get string lengths
    idx1 = len(str1)
    idx2 = len(str2)

    # Pick last char
    s1 = str1[idx1 - 1] if idx1 > 0 else str1
    s2 = str2[idx2 - 1] if idx2 > 0 else str2

    # Compare
    if s1 > s2 or idx1 > idx2:
        return 1
    if s1 < s2 or idx1 < idx2:
        return -1
    if s1 == s2 and (idx1 > 0) == (idx2 > 0):
        s1 = str1[:len(str1) - 1]
        s2 = str2[:len(str2) - 1]
        strcomp(s1, s2)
        return 0


if __name__ == '__main__':
    print(fibonacci(10))
    print(gcd(100, 8))
    print(strcomp('bobby', 'bradbury'))



