# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:34:51 2021

@author: 90730
"""

count = 0
while count<10:
    if count%2==0 and count%4==0 :
        print(".",end="")
    else:
        print("-",end="")
    count +=1