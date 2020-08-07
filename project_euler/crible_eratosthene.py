#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy


class CribleEratosthene:

    def __init__(self, max_val):
        max_val = int(max_val)
        self.max_val = max_val
        self.crible = numpy.array([True] * (max_val + 1))
        self.prime_numbers = []
        self.init_crible()

    def init_crible(self):
        n = 1
        while n < self.max_val:
            n += 1

            while (n < self.max_val) and (self.crible[n] is False):
                print("Skip", n)
                n += 1

            p = 2
            # print("Prime number :", n)
            if self.crible[n]:
                self.prime_numbers.append(n)
            while n * p <= self.max_val:
                # print("Ignore ", n * p)
                self.crible[n * p] = False
                p += 1




