import pygame
import random
import time
from utils import get_image, checkInSnake
from random import randint
from Snake import Snake

# CONFIG
WIDTH = 800
HEIGHT = 600
CAPTION = "Mad Snake"

# GAME SETTINGS
FPS = 120
TARGET_SCORE = 5

LEVELS = [
    {
        'name': 'EASY',
        'colors': [(47, 131, 50),(31, 97, 34)]
    },
    {
        'name': 'NORMAL',
        'colors': [(221, 214, 53),(200, 194, 43)]
    },
    {
        'name': 'HARD',
        'colors': [(242, 186, 40),(222, 170, 37)]
    },
    {
        'name': 'VERY_HARD',
        'colors': [(218, 73, 42),(195, 62, 33)]
    },
    {
        'name': 'INSANE',
        'colors': [(219, 25, 25),(188, 20, 20)]
    },
    {
        'name': 'IMPOSSIBLE',
        'colors': [(0, 0, 0),(0, 0, 0)]
    },
]
ACTIVE_LEVEL = 0

# pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
running = True
game = True
status = 'playing'
# 'playing' | 'defeat' | 'win'
clock = pygame.time.Clock()
score = 0

# Spawn extra food
pygame.time.set_timer(pygame.USEREVENT, 8000)

# RESOURCES
font = pygame.font.Font("PressStart2P-Regular.ttf", 13)    
level = pygame.font.Font("PressStart2P-Regular.ttf", 15)

WHITE = (255, 255, 255)

food_variants = [
    ['food.png', 1],
    ['food2.png', 3]
]
class Food(pygame.sprite.Sprite):
    def __init__(self, snake, group):
        pygame.sprite.Sprite.__init__(self)
        variant = food_variants[randint(0,1)]
        self.snake = snake
        self.width = 20
        self.height = 25
        self.image = pygame.image.load(variant[0])
        self.rect = self.image.get_rect()
        self.weight = variant[1]
        self.add(group)
        self.spawnTime = int(time.time())
        self.spawn()

    def spawn(self):
        x = random.randint(self.width+10, WIDTH-self.width-10)
        y = random.randint(50, HEIGHT-self.height-10)
        while checkInSnake(self.snake.parts, 15, x): x = random.randint(10, WIDTH-10)
        while checkInSnake(self.snake.parts, 15, y): y = random.randint(50, HEIGHT-10)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(x = x, y = y)

    def update(self):
        if int(time.time()) - self.spawnTime > 5:
            self.kill()

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

snake = Snake(WIDTH/2, HEIGHT-200)
snake.color_head = LEVELS[ACTIVE_LEVEL]['colors'][1]
snake.color_body = LEVELS[ACTIVE_LEVEL]['colors'][0]

food = False

foods = pygame.sprite.Group()
food = Food(snake, foods)
print(food.get_rect())

def gameRestart():
    global score, ACTIVE_LEVEL, status, FPS, snake, food
    score = 0
    ACTIVE_LEVEL = 0
    status = 'playing'
    FPS = 120
    snake.restart()
    food = False

# CYCLE
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            gameRestart()
        if event.type == pygame.USEREVENT:
            Food(snake, foods)

        snake.events(event)

    # Update
    foods.update()
    if not snake.update() and status != 'win':
        # Game over
        game = False
        status = 'defeat'
        snake.stop()
        snake.color_head = (255, 0, 0)
    else:
        game = True
        status = 'playing'

        # Check collide snake with food
        foodCollide = pygame.Rect.collidelist(snake.get_rect(), [x.get_rect() for x in foods.sprites()])
        if foodCollide != -1:
            sprite = foods.sprites()[foodCollide]
            snake.grow()
            score += sprite.weight
            foods.remove(sprite)
            Food(snake, foods)

        # Change levels
        if score != 0 and score >= (ACTIVE_LEVEL+1) * TARGET_SCORE:
            # WIN
            if ACTIVE_LEVEL == len(LEVELS)-1:
                game = False
                snake.stop()
                status = 'win'
            # NEXT LEVELS
            else:
                ACTIVE_LEVEL += 1
                FPS += 50
                if ACTIVE_LEVEL == len(LEVELS)-1:
                    snake.enableRainbow()
                else:
                    snake.color_head = LEVELS[ACTIVE_LEVEL]['colors'][1]
                    snake.color_body = LEVELS[ACTIVE_LEVEL]['colors'][0]
            


    # Render
    screen.fill(WHITE)

    snake.render(screen)
    foods.draw(screen)

    # GUI
    screen.blit(get_image('score.png'), (15, 15))
    score_label = font.render(str(score), True, (86, 77, 0))
    level = font.render(LEVELS[ACTIVE_LEVEL]['name'], True, LEVELS[ACTIVE_LEVEL]['colors'][1])
    screen.blit(score_label, (100, 15))
    screen.blit(level, level.get_rect(center=(WIDTH/2, 20)))

    if status == 'defeat':
        screen.blit(get_image('game_over.png'), (215, 206))
    if status == 'win':
        screen.blit(get_image('win.png'), (111, 117))
    
    pygame.display.flip()
    clock.tick(FPS)