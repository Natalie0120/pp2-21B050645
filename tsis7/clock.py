import pygame
import os

import time

WIDTH = 832
HEIGHT = 836

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")
done = False
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        screen.blit(get_image('assets/clock/clock_base.png'), (0, 0))


        curr_min = time.localtime().tm_min
        curr_sec = time.localtime().tm_sec
        
        arrow_sec = get_image('assets/clock/clock_sec.png')
        arrow_min = get_image('assets/clock/clock_min.png')
        blitRotateCenter(screen, arrow_sec, (0,0), -curr_sec*6)
        blitRotateCenter(screen, arrow_min, (0,0), -curr_min*6)
        
        pygame.display.flip()
        clock.tick(60)