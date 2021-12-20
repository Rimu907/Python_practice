# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 22:38:00 2020

@author: 90730
"""

import pygame,sys
speed = [1,1]
Background = 255,255,255
blue = 0, 0, 255
purple = 128,0,128
white=255,255,255
width,height=1600,900
FPS = 144
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('pygame!!!!')
ball = pygame.image.load('giphy.gif', 'r')
ballrect = ball.get_rect()
pygame.mixer.init()
pygame.mixer.music.load('A:/pythonstudy--/Time.mp3')
pygame.mixer.music.play()
fclock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0]=speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0]=speed[0]+1 if speed[0]>0 else speed[0]-1
            elif event.key == pygame.K_UP:
                speed[1]=speed[1]+1 if speed[1]>0 else speed[1]-1
            elif event.key == pygame.K_DOWN:
                speed[1]=speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1]/abs(speed[1]))
                
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left<0 or ballrect.right > width:     
        speed[0] =-speed[0]
        Background=blue
        
    if ballrect.top<0 or ballrect.bottom > height:               
        speed[1] =-speed[1]       
        Background=purple
  
    screen.fill(Background)
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(FPS)