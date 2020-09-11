#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 20:37:16 2020

@author: deepak
"""

""" Finding the Roots of a Quadratic Equation """

def roots(a,b,c):
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)
    
    print("x_1 : {0}".format(x_1))
    print("x_2 : {0}".format(x_2))
    
if __name__ == '__main__':
    a = input("Enter a : ")
    b = input("ENter b : ")
    c = input("Enter c : ")
    roots(float(a),float(b),float(c))
    
    