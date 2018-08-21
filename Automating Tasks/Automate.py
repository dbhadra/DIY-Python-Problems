#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:10:03 2018

@author: deepayanbhadra
"""

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
    