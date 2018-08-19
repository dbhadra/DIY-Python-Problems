#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 20:21:44 2018

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
        
def comma_code(user_list):
    str_op = user_list[0]
    l = len(user_list)
    for i in range(1,l-1):
        str_op += ','+user_list[i]
    str_op+=' and '+user_list[l-1]
    return str_op

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v,k)
        item_total+=v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory,addedItems):
    
    
        
if __name__ == "__main__":
    
    x = int(input("Enter a number: "))
    while x is not 1:
        x = collatz(x)
    
    user_list = input("Enter list elements separated by comma ")
    user_list  = user_list.split(",")    
    str_op = comma_code(user_list)
    
    grid = input("Enter list elements separated by comma ")
    grid = grid.split()
    
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(stuff)
    