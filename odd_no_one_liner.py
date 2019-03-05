#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:33:21 2019

@author: gurpreets

One Liner for loop
"""

# Odd numbers between a range:
a = int(input("Enter start value:"))
b = int(input("Enter end value:"))
print([i for i in range(a,b+1) if i%2 != 0])

# Multi for loops
print([(x, y) for x in [3,6,9] for y in [3,1,4] if x != y])