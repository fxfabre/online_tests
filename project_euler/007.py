#!/usr/bin/python3
# -*- coding: utf-8 -*-

from crible_eratosthene import CribleEratosthene

ce = CribleEratosthene(110000)
print(len(ce.prime_numbers))
if len(ce.prime_numbers) > 10001:
    print(ce.prime_numbers[10000])


