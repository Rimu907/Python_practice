# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:48:43 2021

@author: 90730
"""

lst = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(lst)-1,-1,-2):
        print(lst[i],end=",")
print()
for i in range(len(lst)-2,-1,-2):
     print(lst[i],end=",")

