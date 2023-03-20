import pygame
import os

import time

WIDTH = 800
HEIGHT = 600
RADIUS = 25

WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Just Circle")
done = False
clock = pygame.time.Clock()

x, y = WIDTH/2, HEIGHT/2
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y > RADIUS: y -= 20
        if pressed[pygame.K_DOWN] and y < HEIGHT - RADIUS: y += 20
        if pressed[pygame.K_LEFT] and x > RADIUS: x -= 20
        if pressed[pygame.K_RIGHT] and x < WIDTH - RADIUS: x += 20
        
        screen.fill(WHITE)
        pygame.draw.circle(screen, RED, (x, y), RADIUS)
        
        pygame.display.flip()
        clock.tick(60)