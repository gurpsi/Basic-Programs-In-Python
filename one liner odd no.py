#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:01:31 2019

@author: gurpreets
"""

a,b = input().split(' ')
print([i for i in range(int(a),int(b)+1) if i%2 != 0])