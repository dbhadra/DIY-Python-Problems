#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:53:37 2018

@author: deepayanbhadra
"""
import sys
def collatz(number):
    if number%2 == 0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return(3*number+1)

if __name__ == "__main__":
    x = int(input("Enter a number: "))
    while x is not 1:
        x = collatz(x)

# EOF
        

    
        