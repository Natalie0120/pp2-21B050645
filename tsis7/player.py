import pygame
import os

pygame.init()

WIDTH = 250
HEIGHT = 500

WHITE = (255, 255, 255)

# Font
fontBold = pygame.font.Font("assets/player/Blinker-SemiBold.ttf", 15)
font = pygame.font.Font("assets/player/Blinker-Regular.ttf", 13)

subtitle = font.render('playing now', True, WHITE)
song_name = fontBold.render('BoyWithUke-Toxic', True, WHITE)

# Images
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

# Songs
song_path = 'assets/player/songs/'
songs = os.listdir(song_path)
NUM_OF_SONG = len(songs)
CURRENT_SONG = 0
SONG_PLAYING = False
def setSong(index):
    global songs, CURRENT_SONG, song_name, SONG_PLAYING
    song = songs[index]
    pygame.mixer.music.load(song_path+song)
    pygame.mixer.music.play()
    if not SONG_PLAYING: pygame.mixer.music.pause()
    CURRENT_SONG = index
    song_name = fontBold.render(song[:-4], True, WHITE)
    print('Now playing '+song[:-4])

def playHandler():
    global SONG_PLAYING
    if SONG_PLAYING: 
        pygame.mixer.music.pause()
        SONG_PLAYING = False
    else:
        pygame.mixer.music.unpause()
        SONG_PLAYING = True

# Presses
left_press = False
right_press = False
def presses(event):
    global left_press, right_press

    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        left_press = True
    else: left_press = False

    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        right_press = True
    else: right_press = False


# Main
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pyPlayer")
pygame.display.set_icon(pygame.image.load('assets/player/icon.png'))

done = False
clock = pygame.time.Clock()

setSong(0)
pygame.mixer.music.pause()

while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            presses(event)
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                next_song = CURRENT_SONG - 1
                if next_song < 0: next_song = NUM_OF_SONG-1
                setSong(next_song)

            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                next_song = CURRENT_SONG + 1
                if next_song >= NUM_OF_SONG: next_song = 0
                setSong(next_song)

            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                playHandler()
                
    
    screen.fill((28, 36, 49))
    screen.blit(get_image('assets/player/screen.png'), (15, 15))
    screen.blit(subtitle, (28, 165))
    screen.blit(song_name, (28, 185))

    screen.blit(get_image('assets/player/play.png'), (50, 290))
    screen.blit(get_image('assets/player/left.png'), (5, 300))
    screen.blit(get_image('assets/player/right.png'), (185, 300))

    if (left_press): screen.blit(get_image('assets/player/left_press.png'), (5, 300))
    if (right_press): screen.blit(get_image('assets/player/right_press.png'), (185, 300))
    if (SONG_PLAYING): screen.blit(get_image('assets/player/play_active.png'), (50, 290))

    pygame.display.flip()
    clock.tick(120)