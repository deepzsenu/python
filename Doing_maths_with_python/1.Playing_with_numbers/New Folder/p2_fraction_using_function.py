#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:51:27 2020

@author: deepak
"""
''' 
Find the factors of an integer
'''
def factors(b):
    for i in range(1, b+1):
        if b % i == 0:
            print(i)
            
if __name__ == '__main__':
    b = input('Your Number please : ')
    b = float(b)
    
    if b>0 and b.is_integer():
        factors(int(b))
        
    else:
        print('Print a positive integer')
    
