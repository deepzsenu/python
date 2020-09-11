#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 20:16:09 2020

@author: deepak
"""

#the program for our multiplication table printer:
    
def multi_table(a):
    for i in range(1,11):
        print('{0} X {1} = {2}'.format(a, i, a*i))
        
if __name__ == '__main__':
    a = input("Enter the number whose table you want to print : ")
    multi_table(float(a))
    