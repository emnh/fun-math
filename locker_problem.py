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

def main():
    # False is closed, True is open
    sieve = [False for x in range(1001)]
    for i in range(1, 1001):
        for j in range(1, 1001, i):
            sieve[j] = not sieve[j]
    solution = []
    for i in range(1, 1001):
        if sieve[i]:
            solution.append(i - 1)
    print(*solution)

if __name__ == '__main__':
    main()

