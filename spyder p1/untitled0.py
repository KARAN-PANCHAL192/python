# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 12:53:27 2022

@author: HP
"""

import keyword
x=["except","raise","fall"]
for i in range(len(x)):
    if keyword.iskeyword(x[i]):
        print(x[i],"true")
    else:
        print(x[i],"false")
    
              
              
              
              
              
              
              
    