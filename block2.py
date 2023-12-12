#블록깨기_2

import random
import pygame

pygame.init()
background = pygame.display.set_mode((480,360))
pygame.display.set_caption("Brick breaking")

size_width_bg = background.get_size()[0]
size_height_bg = background.get_size()[1]

size_width_pedal = 100
size_height_pedal = 15

x_pos_pedal = size_width_bg // 2 - size_width_pedal // 2
y_pos_pedal = size_height_bg - size_height_pedal

rect_pedal = pygame.Rect(x_pos_pedal,y_pos_pedal,size_width_pedal,size_height_pedal)

size_radius_ball = 20

x_pos_ball = size_height_bg // 2
y_pos_ball = size_height_bg - size_height_pedal - size_radius_ball

rect_ball = pygame.Rect(x_pos_ball,y_pos_ball,size_radius_ball * 2,size_radius_ball * 2)
rect_ball.center = (x_pos_ball, y_pos_ball) 

size_width_block = size_width_bg // 10
size_height_block = 30

x_pos_block = 0
y_pos_block = 0

rect_block = [[] for _ in range(10)]
color_block = [[] for _ in range(10)]

for i in range(10):
    for j in range(3):
        rect_block[i].append(pygame.Rect(i * size_width_block, j * size_height_block, size_width_block,size_height_block))
        color_block[i].append((random.randrange(225), random.randrange(150,225), random.randrange(150,225)))

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    background.fill((225,225,225))
    
    pygame.draw.rect(background, (225,225,0), rect_pedal)
    
    pygame.draw.circle(background, (225,0,225),(x_pos_ball,y_pos_ball),size_radius_ball)        

    for i in range(10):
        for j in range(3):
            if rect_block[i][j]:
                pygame.draw.rect(background, color_block[i][j], rect_block[i][j])
                
    pygame.display.update()

pygame.quit()