#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:24:39 2020

Lecture 24:  Pygame II
based on code by pszit
@author: psztxa
"""

import pygame
import os

# Global variables
WIDTH = 1200
HEIGHT = 600
BORDER = 40
VELOCITY = 5
FRAMERATE = 50

# define my classes

class Ball:
    RADIUS=20
    
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.moving = False

    def show(self,colour):
        global screen
        pygame.draw.circle(screen, colour, (self.x,self.y),self.RADIUS)
    
    def move(self):
        global fg_color,bg_color,paddle, points, lives
        
        if not self.moving :
            return
        new_x = self.x+self.vx
        new_y = self.y+self.vy
        if new_x < BORDER+Ball.RADIUS:
            self.vx = -self.vx
            #pong.play()
        elif new_y < BORDER+Ball.RADIUS or new_y > HEIGHT-BORDER-Ball.RADIUS :
            self.vy = -self.vy
            #pong.play()
        elif new_x > WIDTH-Paddle.WIDTH-self.RADIUS : 
            if abs(self.y-paddle.y) <= Paddle.HEIGHT//2 :
                self.vx = -self.vx # gain a point
                points += 1
                #pong.play()
            else :
                self.moving = False # lost ball
                lives -= 1
        else:
            self.show(bg_color)
            self.x = new_x
            self.y = new_y
            self.show(fg_color)
        
class Paddle:
    
    HEIGHT = 100
    WIDTH = 20
    
    def __init__(self,y) :
        self.y = y

    def show(self,colour) :
        global screen
        
        pygame.draw.rect(screen,colour, 
                         pygame.Rect(WIDTH-self.WIDTH,
                                     self.y-self.HEIGHT//2,
                                     self.WIDTH,self.HEIGHT))
        
    def update(self) :
        global fg_color
        new_y = pygame.mouse.get_pos()[1]
        if new_y >= BORDER+self.HEIGHT//2 \
           and new_y <= HEIGHT-BORDER-self.HEIGHT//2 :
            self.show(bg_color)
            self.y = new_y
            self.show(fg_color)

def show(text) :
    myFont = pygame.font.SysFont(pygame.font.get_default_font(),40)
    surf = myFont.render(text,False,bg_color,fg_color)
    screen.blit(surf,(0,0))

# initialising pygame
pygame.init()

#pong = pygame.mixer.Sound("pong.wav")

lives = 3
points = 0

clock = pygame.time.Clock()

# creating the display with WIDTH and HEIGHT
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Fill the background of the object (Surface)
bg_color = pygame.Color("blue")
fg_color = pygame.Color("white")

screen.fill(bg_color)

# Drawing the walls
pygame.draw.rect(screen,fg_color, pygame.Rect(0,0,WIDTH,BORDER))
pygame.draw.rect(screen,fg_color, pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))
pygame.draw.rect(screen,fg_color, pygame.Rect(0,0,BORDER,HEIGHT))

# draw a ball
# RADIUS = 20
# 
ball = Ball(WIDTH-Ball.RADIUS-Paddle.WIDTH,HEIGHT//2,-VELOCITY,-VELOCITY)
ball.show(fg_color)

# paddle

paddle = Paddle(HEIGHT//2)
paddle.show(fg_color)

# This while loop awaits for events... Whenever the user closes the window 
# (that's a QUIT event) the loop will break
while lives > 0:
    show(F"lives = {lives} , points = {points}")
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    elif e.type == pygame.MOUSEBUTTONDOWN :
        ball.moving = True

    # Every time we draw something on a surface... we need to flip it on the screen.
    pygame.display.flip()
    ball.move()
    paddle.update()
    clock.tick(FRAMERATE)
    
print(F"You got : {points}")

pygame.quit() # for the rest of the people with windows or Linux
os._exit(0) # for Mac users.