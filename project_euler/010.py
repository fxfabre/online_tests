#!/usr/bin/python3
# -*- coding: utf-8 -*-

from crible_eratosthene import CribleEratosthene

ce = CribleEratosthene(2e6)

print(len(ce.prime_numbers))
print(sum(ce.prime_numbers))
