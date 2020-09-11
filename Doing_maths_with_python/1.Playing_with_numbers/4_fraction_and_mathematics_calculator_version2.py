#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:30:57 2020

@author: deepak
"""


from fractions import Fraction
def add(a, b):
    print('Result of adding {0} and {1} is {2} '.format(a, b, a+b))

def subtract(a, b):
    print('Result of subtracting {1} from {0} is {2}'.format(a, b, a-b))

def divide(a, b):
    print('Result of dividing {0} by {1} is {2}'.format(a, b, a/b))

def multiply(a, b):
    print('Result of multiplying {0} and {1} is {2}'.format(a, b, a*b))

if __name__ == '__main__':

    while True:

        try:
            a = Fraction(input('Enter first fraction: '))
            b = Fraction(input('Enter second fraction: '))
            op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
            if op == 'Add' or op=='add':
                add(a, b)
            if op == 'Subtract' or op == 'substract':
                subtract(a, b)
            if op == 'Divide' or op == 'divide':
                divide(a, b)
            if op == 'Multiply' or op = 'multiply':
                multiply(a, b)
        except ValueError:
            print('Invalid fraction entered')
        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break