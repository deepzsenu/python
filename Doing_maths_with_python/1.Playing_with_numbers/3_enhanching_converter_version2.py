#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:22:26 2020

@author: deepak
"""

def print_menu():
    print("MENU")
    print("Please Enter your Choise")
    print("1. Kilometer to Miles")
    print("2. Miles to Kilometer")
    print("3.kilograms to pound")
    print("4.pounds to kilogrm")
    print("5.celcius to fherenheit")
    print("6.fherenheit to celcius")
    
def km_miles():
    km = float(input("Enter in kilometers : "))
    miles = km/1.609
    print('Distance in Miles is {0}'.format(miles))
    
def miles_km():
    miles = float(input("Enter in Miles : "))
    km1 = 1.609*miles
    print("Distance in Kilometers in : {0}".format(km1))

def kg_pd():
    kg = float(input("Enter The weight in Kilograms : "))
    pd = kg*2.206
    print("Weight in pounds is : {0}".format(pd))
    
def pd_kg():
    pd = float(input("Enter the weight in Pounds : "))
    kg = pd/2.206
    print("THe weight in Kilograms is : {0}".format(kg))
    
def cel_fher():
    cel = float(input("Enter the Temprature in celcius : "))
    fher = (cel*(9/5))+32
    print("The temprature in Fherenheit is : {0}".format(fher))
    
def fher_cel():
    fher =  float (input("Enter the Temprature in Fherenhiet : "))
    cel = (fher-32)*(5/9)
    print("The temprature in celcius is : {0}".format(cel))
    
if __name__ == '__main__':
    print_menu()
    
    while True:
        
        choise = input("Which conversion do you want : ")
        if choise == '1':
            km_miles()
        
        if choise == '2':
            miles_km()
        
        if choise == '3':
            kg_pd()
        
        if choise == '4':
            pd_kg()
        
        if choise == '5':
            cel_fher()
        
        if choise == "6":
            fher_cel()
            
        answer = str(input("Do you want to exit press Y for exit :  "))
        if answer == 'y' or answer == 'Y':
            break
        