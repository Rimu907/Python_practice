# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:44:31 2020

@author: 90730
"""

import pygame,sys

class Ball: 
    
    RADIUS = 10
    
    def __init__(self, x,y, vx, vy):
        self.x = x
        self.y = y 
        self.vx = vx
        self.vy = vy
        
    def show(self, colour):
        global screen
        pygame.draw.circle(screen, colour,\
                           (self.x, self.y),\
                           self.RADIUS)
        
    def update(self):
     
        newx = self.x + self.vx
        newy = self.y + self.vy
        
        if newy < BORDER or newy > HEIGHT-BORDER:
            self.vy = -self.vy
        elif newx < BORDER:
            self.vx = -self.vx
        else:
            # change the colour
            self.show(pygame.Color("black"))
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(pygame.Color("white"))
            
WIDTH,HEIGHT=1200,900
BORDER = 40
VELOCITY = 4
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(pygame.Color("blue"))

pygame.draw.rect(screen, pygame.Color("white"),\
                 pygame.Rect(0,0,WIDTH, BORDER))
pygame.draw.rect(screen, pygame.Color("white"),\
                 pygame.Rect(0,0,BORDER, HEIGHT))
pygame.draw.rect(screen, pygame.Color("white"),\
                 pygame.Rect(0,HEIGHT-BORDER,WIDTH,\
                             BORDER))

ball = Ball(WIDTH-Ball.RADIUS, HEIGHT//2,\
            -VELOCITY, 0)
ball.show(pygame.Color("white"))

pygame.display.flip()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        pygame.quit()
        break
    ball.update()  
    pygame.display.flip()