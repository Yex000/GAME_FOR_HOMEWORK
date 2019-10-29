import pygame
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
        pygame.display.flip()   
        screen_help.blit(background, [0,0])        
    pygame.quit()
