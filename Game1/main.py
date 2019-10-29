import pygame
import random
import checker
import winner, loser

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
score = 0
flag = False
position = 0
hearts = 3


class NUMBER(pygame.sprite.Sprite):
    def __init__(self):
        '''return random generated number from 1 to 100 on image on the screen'''
        super(NUMBER, self).__init__()
        self.surf = pygame.Surface((40, 40))
        self.surf = pygame.image.load("image/rubbish.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(20, SCREEN_WIDTH-20), -25
                   )
        )
    def update(self, pressed_keys):
        ''' check if player has pressed
         a key and then make appropriate movement
        '''
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
        if self.rect.bottom > SCREEN_HEIGHT-400:
            global spawn_player
            spawn_player = True
            global flag
            flag = True
            global position
            position = self.rect.right

def dumps(variant):
    '''change white parts of game object on transparent one''' 
    image = pygame.image.load("{0}.png".format(variant)).convert()
    image.set_colorkey((255, 255, 255), RLEACCEL)
    return image


pygame.init()

font = pygame.font.SysFont('Impact', 32) 
text_esc = font.render('Press ESC to Quit', True, (0 ,0 ,128 ))  
text_esc_rect = text_esc.get_rect(center = (120, 25))

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

#hearts making
heart1 = pygame.Surface((50, 50))
heart1 = pygame.image.load("image/heart.png").convert()
heart1.set_colorkey((0, 0, 0), RLEACCEL)
heart1_rect = heart1.get_rect()
heart1_rect = heart1_rect.move((550, 40))

heart2 = pygame.Surface((50, 50))
heart2 = pygame.image.load("image/heart.png").convert()
heart2.set_colorkey((0, 0, 0), RLEACCEL)
heart2_rect = heart2.get_rect()
heart2_rect = heart2_rect.move((500, 40))

heart3 = pygame.Surface((50, 50))
heart3 = pygame.image.load("image/heart.png").convert()
heart3.set_colorkey((0, 0, 0), RLEACCEL)
heart3_rect = heart3.get_rect()
heart3_rect = heart3_rect.move((450, 40))

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
    text_player = font.render(str(number), True, (0, 255, 0 ))
    text_player_rect = text_player.get_rect(
        center = (new_player.rect.right - 33, new_player.rect.top + 53)
    )

    text_score = font.render('Your score: {}'.format(score), True, (160 ,0 ,0 ))  
    text_score_rect = text_esc.get_rect(center = (SCREEN_WIDTH - 60, 25))

    

    # Fill the background with background
    screen.blit(background_image, [0, 0])
    screen.blit(new_player.surf, new_player.rect)
    screen.blit(text_score, text_score_rect)
    screen.blit(text_player, text_player_rect)
    screen.blit(text_esc, text_esc_rect)
    
    if hearts == 3:
        screen.blit(heart1, [550, 40])
        screen.blit(heart2, [500, 40])
        screen.blit(heart3, [450, 40])

    elif hearts == 2:
        screen.blit(heart1, [550, 40])
        screen.blit(heart2, [500, 40])

    elif hearts == 1:
        screen.blit(heart1, [550, 40])

    else:
        loser.loser()    
    # Draw dumps
    for x in enumerate([0, 151, 302, 453]):
        dump = dumps(x[0] + 1) # makes dump
        screen.blit(dump, (x[1], 460))


    if flag:
        flag = False
        check = checker.check(position, number)
        if check:
            score += 1
        else:
            hearts-=1
            
    if score == 15:
        winner.winner()        

    # Flip the display
    pygame.display.flip()
    speed_game += asseleration
    clock.tick(speed_game)

# Done! Time to quit.
#pygame.quit()