# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:52:12 2020

@author: 90730
"""
def ham(l):
    s=[]
    for x in l:
        s=[x]+s
    return s

m=[1,2,3,4]
result = ham(m)
print(result) 