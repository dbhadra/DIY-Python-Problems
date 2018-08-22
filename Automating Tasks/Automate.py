#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:10:03 2018

@author: deepayanbhadra
"""

# Pattern Matching

import re
def password_detect(exp):
    if len(exp) >= 8:        
        passRegex = re.compile(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])")
        mo = passRegex.search(exp)
        if mo != None:
            print("Password is strong")
        else:
            print("Password is not strong")
        
    else:
        print("Password length is not strong")


def find_websites(exp):
    webRegex = re.compile(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)")
    mo = webRegex.search(exp)
    if mo != None:
        print("Website found")
        mo.group()
    else:
        print("No website found")    