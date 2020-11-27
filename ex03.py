# -*- coding: utf-8 -*-
"""
Created on Fri Oct  30 16:10:45 2020

@author: NANDI GUO
"""
SIZE = 20                                                    #Set the board size
count = 0                                                   #count default = 0
if SIZE < 4:                                                #if size<4, it's Meaningless
    print('Board size should bigger than 3') 
else:   
    def empty_grid() :                                      #for creating a board
        global grid
        grid=[]                                             #grid=[] in this step
        for i in range(SIZE) :
            y=[]                                            #y=[][][][][]...... in this step
            for j in range(SIZE) :
                y = y+['.']                                 #y=['.','.','.','.']['.','.','.','.']...... in this step
            grid=grid+[y]                                   #grid=[['.','.','.','.'...],['.','.','.',','...]... ]in this step
                       
    def solve(grid,y):                        
        global count
        for x in range(0,SIZE):                             #horizontal check from 0->size
            if  possible(grid,y,x):                         #if true
                #print(y,x)            
                grid[y][x]='Q'                              #make this coordinate (y,x) = Q    
                solve(grid, y+1)                            #Backtracking,y+1 means move down in vertical direction 
                grid[y][x]='.'                              #if can't, make that coordinate be '.'
       
        if y == SIZE:                                       #Recursion limit, if all 0->size have done
            count += 1                                   
            print(count)                                    
            for m in grid:                                
                print(' '.join(m))                          #show results in grid, ' '.join is to beautify board
            input('more?')                                
            
    def possible(grid,y,x):
        for i in range(0,SIZE):                             #vertical check, horizontal x keep same
            if grid[i][x]=='Q':                             #if veritical got Q then return false
                return False
        for i,j in zip(range(y-1,-1,-1),range(x+1,SIZE,1)): #direction: 45° slash, Traverse y and x at same time by using zip.     
            if grid[i][j]=='Q':                             #Get every coordinates on the slash, if == Q , return False
                return False                                #vertical from y-1 to -1, -1 everytime, horizontal from x+1 to Size,+1 everytime 
        for i,j in zip(range(y-1,-1,-1),range(x-1,-1,-1)):  #direction: 135° slash, Traverse y and x at same time by using zip.
            if grid[i][j]=='Q':                             #Get every coordinates on the slash, if == Q , return False
                return False                                #vertical from y-1 to -1, -1 everytime, horizontal from x-1 to -1, -1 everytime 
        return True
    
    empty_grid()
    solve(grid,0)                                           #start from 0