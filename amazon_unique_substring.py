#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:56:06 2019

@author: gurpreets
"""


def get_all_substrings(input_string, n):
  length = len(input_string)
  temp = [input_string[i:j+1] for i in range(length) for j in range(i,length)]
  count = 0
  for i in range(len(temp)):
      if (len(temp[i]) >= n and len(list(set(temp[i]))) == n):
          count+=1
          print(temp[i])
          
  
  return count

print (get_all_substrings('abafg', 2))

# Input_string: Is a normal string.
# n: Number of unique characters that should be present in output.