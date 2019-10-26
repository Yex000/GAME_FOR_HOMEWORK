import pygame
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 612
SCREEN_HEIGHT = 900
speed_player = 3
speed_move = 5
spawn_player = True

class NUMBER(pygame.sprite.Sprite):
    def __init__(self):
        super(NUMBER, self).__init__()
        self.surf = pygame.Surface((40, 40))
        self.surf.fill((0, 100, 200))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(20, SCREEN_WIDTH-20), -25
                   )
        )
    def update(self, pressed_keys):
        self.rect.move_ip(0, speed_player)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-speed_move, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(speed_move, 0)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, speed_player*3)
        if self.rect.bottom < SCREEN_HEIGHT:
            self.kill()
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT:
            global spawn_player
            spawn_player = True

def lines():
    surf = pygame.Surface((3, 100))
    surf.fill((0, 0, 0)) #Solid color for lines

    return surf

pygame.init()

font = pygame.font.SysFont('Arial', 32) 
text = font.render('Press ESC to Quit', True, (0 ,0 ,128 ))  
textRect = text.get_rect(center = (100, 25))





clock = pygame.time.Clock()
#add event (spawn)
SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN, 5000)
# Name of the window
pygame.display.set_caption("SortIt")
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_WIDTH])
# Downloading background
background_image = pygame.image.load("background.png").convert()

# Run until the user asks to quit
running = True
#making a player sprite
new_player = NUMBER()


while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
    if spawn_player:
       new_player = NUMBER()
       spawn_player = False
    # reads pressed button 
    pressed_keys = pygame.key.get_pressed()
    # update player's cccoordiantes
    new_player.update(pressed_keys)
    # Fill the background with background
    screen.blit(background_image, [0, 0])

    line = lines() #Get bottom lines

    for x in [150, 303, 456]:
        screen.blit(line, (x, 530))

    screen.blit(new_player.surf, new_player.rect)
    screen.blit(text, textRect)
    # Flip the display
    pygame.display.flip()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()