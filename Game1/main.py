import pygame
import random
import checker

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
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
speed_game = 30
asseleration = 0.01
spawn_player = True
score = 5
flag = False
position = 0


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
        if self.rect.top > SCREEN_HEIGHT - 100:
            self.kill()
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT:
            global spawn_player
            spawn_player = True
            global flag
            flag = True
            global position
            position = self.rect.right

def dumps(variant):
    image = pygame.image.load("{0}.png".format(variant)).convert()
    image.set_colorkey((255, 255, 255), RLEACCEL)
    return image


pygame.init()

font = pygame.font.SysFont('Arial', 32) 
text_esc = font.render('Press ESC to Quit', True, (0 ,0 ,128 ))  
text_esc_rect = text_esc.get_rect(center = (100, 25))

# adds clock for framerate (in the end)
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
        number = random.randint(1,99)
        new_player = NUMBER()
        spawn_player = False

    # reads pressed button 
    pressed_keys = pygame.key.get_pressed()

    # updates player's position
    new_player.update(pressed_keys)

    # makes text with number and attach it to player
    text_player = font.render(str(number), True, (255, 255 ,255 ))
    text_player_rect = text_player.get_rect(
        center = (new_player.rect.right - 20, new_player.rect.top + 22)
    )

    text_score = font.render('Your score: {}'.format(score), True, (160 ,0 ,0 ))  
    text_score_rect = text_esc.get_rect(center = (SCREEN_WIDTH - 50, 25))

    

    # Fill the background with background
    screen.blit(background_image, [0, 0])
    

    screen.blit(new_player.surf, new_player.rect)
    screen.blit(text_score, text_score_rect)
    screen.blit(text_player, text_player_rect)
    screen.blit(text_esc, text_esc_rect)

    # Draw dumps
    for x in enumerate([0, 151, 302, 453]):
        dump = dumps(x[0] + 1) # makes dump
        screen.blit(dump, (x[1], 460))

    if score == 0:
        running = False

    if flag:
        flag = False
        check = checker.check(position, number)
        if check:
            score += 1
        else:
            score -= 1

    # Flip the display
    pygame.display.flip()
    speed_game += asseleration
    clock.tick(speed_game)

# Done! Time to quit.
pygame.quit()