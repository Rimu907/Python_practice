# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:11:04 2021

@author: 90730
"""

def split_and_merge(lista,word):
    word = list(word)
    lista[:] = lista[:3] + word[:3] + lista[3:] + word[3:]
