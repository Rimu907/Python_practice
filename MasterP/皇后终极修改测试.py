# -*- coding: utf-8 -*-
"""
Created on Fri Oct  30 16:10:45 2020

@author: 90730
"""
SIZE = 4
count = 0
if SIZE < 4:
    print('Board size should bigger than 3') 
    
def empty_grid() :
    global grid
    grid=[]
    for i in range(SIZE) :
        y=[]
        for j in range(SIZE) :
            y = y+['.']
        grid=grid+[y]
                   
def solve(grid,y):   
    for x in range(0,SIZE):
        if  possible(grid,y,x):
            #print(y,x)            
            grid[y][x]='Q'            
            solve(grid, y+1)
            grid[y][x]='.'
   
    if y == SIZE:
        global count
        count += 1
        print(count)
        for m in grid:
            print(' '.join(m))   
        input('more?')
        
def possible(grid,y,x):
    for i in range(0,SIZE):
        if grid[i][x]=='Q':
            return False
    
           
                   
    return True

empty_grid()
solve(grid,0)