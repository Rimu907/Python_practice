# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:53:01 2021

@author: 90730
"""

def rev(l) :
    if len(l) == 0: 
        return []
    return rev(l[1:])+[l[0]]

def fib(n):
    if n == 0: 
        return 1
    elif n == 1: 
        return 1
    else: 
        return fib(n-1)+fib(n-2)

rev([1,2,3])

fib(5)
