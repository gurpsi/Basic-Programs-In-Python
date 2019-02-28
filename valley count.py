#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:48:27 2019

@author: gurpreets
"""

#!/bin/python3


# Complete the countingValleys function below.
def countingValleys(n, s):
    #Breaking the steps:
    steps = list(s)
    sea = 0
    valley = 0
    for i in range(n):
        if(str(steps[i]) == 'U' and sea == 0):
            valley-=1
        if(str(steps[i]) == 'D'):
            sea = sea - 1
        elif(str(steps[i]) == 'U'):
            sea = sea + 1
        if (sea == 0):
            valley+=1
    return valley

if __name__ == '__main__':

    n = int(input("Enter number of steps:"))

    s = input("Enter the path as U/D only:")

    result = countingValleys(n, s)
    print("Number of valleys are:", int(result))
