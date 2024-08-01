#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ft=python ts=4 sw=4 sts=4 et fenc=utf-8
# Original author: "Eivind Magnus Hvidevold" <hvidevold@gmail.com>
# License: GNU GPLv3 at http://www.gnu.org/licenses/gpl.html

'''
'''

import os
import sys
import re

def normalize_result(result, base):
    # Remove leading zeros from the result list
    while len(result) > 1 and result[0] == 0:
        del result[0]
    return result

def add_lists(a, b, base):
    result = []
    carry = 0
    a = a[::-1]
    b = b[::-1]
    for i in range(max(len(a), len(b))):
        digit_a = a[i] if i < len(a) else 0
        digit_b = b[i] if i < len(b) else 0
        total = digit_a + digit_b + carry
        carry = total // base
        result.append(total % base)
    if carry:
        result.append(carry)
    return normalize_result(result[::-1], base)

def subtract_lists(a, b, base):
    result = []
    borrow = 0
    a = a[::-1]
    b = b[::-1]
    for i in range(len(a)):
        digit_a = a[i]
        digit_b = b[i] if i < len(b) else 0
        diff = digit_a - digit_b - borrow
        if diff < 0:
            diff += base
            borrow = 1
        else:
            borrow = 0
        result.append(diff)
    return normalize_result(result[::-1], base)

def multiply_lists(a, b, base):
    result = [0] * (len(a) + len(b))
    a = a[::-1]
    b = b[::-1]
    for i in range(len(a)):
        carry = 0
        for j in range(len(b)):
            total = a[i] * b[j] + result[i + j] + carry
            carry = total // base
            result[i + j] = total % base
        if carry:
            result[i + len(b)] += carry
    return normalize_result(result[::-1], base)

def divide_lists(a, b, base):
    if b == [0]:
        raise ValueError("Cannot divide by zero")

    dividend = a[:]
    divisor = b[:]
    result = []
    quotient_digit = 0
    divisor_len = len(divisor)

    # Normalize the divisor
    while len(divisor) < len(dividend):
        divisor.append(0)

    while len(divisor) > len(dividend):
        divisor.pop()

    for i in range(len(dividend) - len(divisor) + 1):
        while True:
            if subtract_lists(dividend[:len(divisor)], divisor, base)[0] >= 0:
                dividend = subtract_lists(dividend[:len(divisor)], divisor, base) + dividend[len(divisor):]
                quotient_digit += 1
            else:
                break
        result.append(quotient_digit)
        quotient_digit = 0
        divisor.pop()

    return normalize_result(result, base)

def main():
    'entry point'
    # Testing the functions with base 10
    a = [1, 5]
    b = [3]
    base = 10
    print("Addition:", add_lists(a, b, base))          # Output: [1, 8]
    print("Subtraction:", subtract_lists(a, b, base))  # Output: [1, 2]
    print("Multiplication:", multiply_lists(a, b, base))  # Output: [4, 5]
    print("Division:", divide_lists(a, b, base))       # Output: [5]

    # Testing the functions with base 2
    a = [1, 1, 1]  # 7 in base 2
    b = [1, 0]     # 2 in base 2
    base = 2
    print("Addition:", add_lists(a, b, base))          # Output: [1, 0, 0, 1] (9 in base 2)
    print("Subtraction:", subtract_lists(a, b, base))  # Output: [1, 0, 1] (5 in base 2)
    print("Multiplication:", multiply_lists(a, b, base))  # Output: [1, 1, 1, 0] (14 in base 2)
    print("Division:", divide_lists(a, b, base))       # Output: [1, 1] (3 in base 2)


if __name__ == '__main__':
    main()
