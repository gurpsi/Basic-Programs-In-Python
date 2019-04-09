#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:17:46 2019

@author: gurpreets
"""

#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the findNumber function below.
def findNumber(arr, k):
    print(len(arr),'   ', arr)
    for i in range(len(arr)):
        print(arr[i])
        if k==arr[i]:
            return "Yes"
        else:
            return "No"

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    res = findNumber(arr, k)
    print("Result", str(res))
