#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:45:11 2020

@author: deepak
"""
#calculating the factors of an inter=ger
def is_factor(a,b):
    if b%a == 0:
        return True
    else:
        return False

print(is_factor(4,1024))
#checking the range function
for i in range(0,100):
    print(i)
