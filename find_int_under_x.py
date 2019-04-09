#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:23:43 2019

@author: gurpreets

Problem:
    
    Find all the combinations of a,b,c,d where
    a^3 + b^3 = c^3 + d^3
"""

def comb(x):
    for i in range(x):
        # print("i:",i)
        for j in range(i+1):
           # print("i,j:",i,j)
            for k in range(j+1):
            #    print("i,j,k:",i,j,k)
                for l in range(k+1):
             #       print("i,j,k,l:",i,j,k,l)
                    if ((pow(i,3)+pow(j,3)) == (pow(k,3) + pow(l,3)) and (i != k or i != l)):
                        print("VALUE:",i,j,k,l)
    
    

x = int(input("Enter the number:"))
comb(x)