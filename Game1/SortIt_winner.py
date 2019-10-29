import pygame
from pygame.locals import(
    KEYDOWN,
    K_ESCAPE
)
def winner():
    
    pygame.init()

    WIDHT = 612
    HEIGHT = 900
    screen_help = pygame.display.set_mode((WIDHT, HEIGHT))

    pygame.display.set_caption("best of the best")
    background = pygame.image.load("image/win_photo.png").convert()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                   running = False
            elif event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False
            elif pygame.mouse.get_pressed()[0] == 1:
                running = False
        pygame.display.flip()   
        screen_help.blit(background, [0,0])        
    pygame.quit()
