#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:53:37 2018

@author: deepayanbhadra
"""

# t is conjectured but not yet proven that no matter which positive integer we start with; we always end up with 1.
import sys
def collatz(number):
    if number%2 == 0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return(3*number+1)

if __name__ == "__main__":
    try:
        x = int(input("Enter a number: "))
        while x is not 1:
            x = collatz(x)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# EOF
        

    
        