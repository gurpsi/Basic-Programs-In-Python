#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:33:21 2019

@author: gurpreets

On Lambda function:
A lambda function can take any number of arguments, but can only have one expression.

Syntax:
    lambda arguments : expression
    
"""
# Lambda:

x = lambda a: a*2
print("X:", x(10))


y = lambda a,b,c : a*b+c
print("Y:",y(2,4,6))
