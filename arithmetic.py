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

def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

def subtract(a, b):
    while b != 0:
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
    return a

def multiply(a, b):
    result = 0
    while b != 0:
        if b & 1:
            result = add(result, a)
        a <<= 1
        b >>= 1
    return result

def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    quotient = 0
    the_sign = (dividend < 0) ^ (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    while dividend >= divisor:
        temp = divisor
        multiple = 1
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dividend = subtract(dividend, temp)
        quotient = add(quotient, multiple)
    return -quotient if the_sign else quotient

def main():
    'entry point'
    # Testing the functions
    a, b = 15, 3
    print("Addition:", add(a, b))          # Output: 18
    print("Subtraction:", subtract(a, b))  # Output: 12
    print("Multiplication:", multiply(a, b))  # Output: 45
    print("Division:", divide(a, b))       # Output: 5

if __name__ == '__main__':
    main()

