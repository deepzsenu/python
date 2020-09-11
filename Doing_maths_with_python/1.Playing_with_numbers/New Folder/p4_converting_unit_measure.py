#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 20:23:41 2020

@author: deepak
"""

'''Here we will convert mile to km and other units'''

def print_menu():
    print("MENU")
    print("Please Enter your Choise")
    print("1. Kilometer to Miles")
    print("2. Miles to Kilometer")
    
def km_miles():
    km = float(input("Enter in kilometers : "))
    miles = km/1.609
    print('Distance in Miles is {0}'.format(miles))
    
def miles_km():
    miles = float(input("Enter in Miles : "))
    km1 = 1.609*miles
    print("Distance in Kilometers in {0}".format(km1))
    
if __name__ == '__main__':
    print_menu()
    choise = input("Which conversion do you want : ")
    if choise == '1':
        km_miles()
        
    if choise == '2':
        miles_km()
        
    else:
        print("You Entered THe wrong  Input")
