# DIFFERENT COIN WEIGHTS
# NEED TO ADD SPEED WHEN REACHING N COINS 
import random, sys,pygame
pygame.init()
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5
ENEMY_STEP = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCORE  = 0
SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # установление экрана
pygame.display.set_caption("Racer game") #название экрана
clock = pygame.time.Clock()
global NUM_OF_COINS
NUM_OF_COINS = 0
score_font = pygame.font.SysFont("Verdana", 20) #шрифт для счетчиков
bg = pygame.image.load("road.jpg") #background

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 
    def update(self):
        global SCORE,ENEMY_STEP
        self.rect.move_ip(0, ENEMY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1 # если энеми проехал всю высоту экрана, это плюс к скору
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('coin.jpg')
        self.image=pygame.transform.scale(self.image,(25,25))
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)
    def update(self):
        self.rect.move_ip(0,5)
        if(self.rect.bottom>SCREEN_HEIGHT):
            self.top=0
            self.rect.center=(random.randint(30,350),0)
    def spawn(self):
        self.rect.center=(random.randint(30,350),0)
    def draw(self,surface):
        surface.blit(self.image,self.rect)

class BIGCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('coin.jpg')
        self.image=pygame.transform.scale(self.image,(45,45))
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(45,SCREEN_WIDTH-45),0)
    def update(self):
        self.rect.move_ip(0,5)
        if(self.rect.bottom>SCREEN_HEIGHT):
            self.top=0
            self.rect.center=(random.randint(30,350),0)
    def spawn(self):
        self.rect.center=(random.randint(30,350),0)
    def draw(self,surface):
        surface.blit(self.image,self.rect)

class Treasure(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('megacoin.jpg')
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(50,SCREEN_WIDTH-50),0)
    def update(self):
        self.rect.move_ip(0,5)
        if(self.rect.bottom>SCREEN_HEIGHT):
            self.top=0
            self.rect.center=(random.randint(30,350),0)
    def spawn(self):
        self.rect.center=(random.randint(30,350),0)
    def draw(self,surface):
        surface.blit(self.image,self.rect)
P1 = Player()
E1 = Enemy()
C1=Coin()
C2=BIGCoin()
T1=Treasure()

enemies = pygame.sprite.Group()
enemies.add(E1)
#adding coins to the sprite group
coins=pygame.sprite.Group()
coins.add(C1)
Bcoins=pygame.sprite.Group()
Bcoins.add(C2)
Treas=pygame.sprite.Group()
Treas.add(T1)

k = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.update()
    C1.update()
    C2.update()
    T1.update()
    if pygame.sprite.spritecollideany(P1, coins):
       NUM_OF_COINS += 1
       if NUM_OF_COINS >= k * 15:
           ENEMY_STEP += 1
           k += 1
       C1.spawn() #как только игрок тронул монету, нужно создать новую
    if pygame.sprite.spritecollideany(P1, Bcoins):
       NUM_OF_COINS += 5
       if NUM_OF_COINS >= k * 15:
           ENEMY_STEP += 1
           k += 1
       C2.spawn()
    if pygame.sprite.spritecollideany(P1, Treas):
       NUM_OF_COINS += 10
       if NUM_OF_COINS >= k * 15:
           ENEMY_STEP += 1
           k += 1
       T1.spawn() 
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.quit()
        sys.exit()
    SURF.blit(bg, (0, 0))
    score_img = score_font.render('Number of passing cars: '+str(SCORE), True, BLACK)
    coin_score_img=score_font.render('Number of collected coins: '+str(NUM_OF_COINS),True,BLACK)
    speed_img=score_font.render('Enemy speed: '+ str(ENEMY_STEP),True,BLACK)
    SURF.blit(score_img, (10, 10)) #позиция счетчика машин
    SURF.blit(coin_score_img,(30,30)) #позиция счетчика монет
    SURF.blit(speed_img,(50,50))
    E1.draw(SURF)
    P1.draw(SURF)
    C1.draw(SURF)
    C2.draw(SURF)
    T1.draw(SURF)
    pygame.display.update()
    clock.tick(FPS)