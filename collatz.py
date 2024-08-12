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

def collatz_sequence(n):
    # Check if the input is a positive integer
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    sequence = [n]  # Start the sequence with the initial value

    # Loop until we reach 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # If n is even, divide by 2
        else:
            n = 3 * n + 1  # If n is odd, multiply by 3 and add 1

        sequence.append(n)  # Append the new value to the sequence

    return sequence

def main():
    'entry point'

    # Example usage:
    #n = 9  # Replace with any positive integer
    for i in range(100):
        n = 3 ** i
        sequence = collatz_sequence(n)
        print(len(sequence))
        #print(f"Collatz sequence starting from {n}: {sequence}")

if __name__ == '__main__':
    main()


