#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 23:20:15 2019

@author: gurpreets
"""

class polygon():
    
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def input_sides(self):
        self.sides = [float(input("Enter Sides "+str(i+1)+":")) for i in range(self.n)]
        
    def dispSides(self):
        for i in range(self.n):
            print("Side is:",self.sides[i])
    
class Triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)
        
    def area(self):
        a,b,c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print("Area of triangle is:", area)
        

t = Triangle()
t.input_sides()
t.dispSides()
t.area()