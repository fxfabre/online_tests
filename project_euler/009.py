#!/usr/bin/python3
# -*- coding: utf-8 -*-


for a in range(1001):
    for b in range(1001-a):
        c = 1000 - a - b
        if a * a + b * b == c * c:
            print(a, b, c, a * b * c)


