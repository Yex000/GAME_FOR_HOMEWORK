import pygame
import random
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    )
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000



clock = pygame.time.Clock()
pygame.init()



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
            # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
    # Fill the screen with black

    for i in [175, 500, 825]:
        platform = pygame.Surface((300, 50))
        platform.fill((255, 255, 255))
        platform.get_rect(
            center=(
                i, SCREEN_HEIGHT - 50
                   )
            )
        screen.blit(platform, platform.get_rect())
    
    screen.fill((25, 50, 50))
    pygame.display.flip()
    clock.tick(30)

