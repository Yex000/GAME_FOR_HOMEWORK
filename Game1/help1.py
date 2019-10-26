import pygame
def help_fn():

    from pygame.locals import(
    RLEACCEL
    )
    
    pygame.init()

    WIDHT = 612
    HEIGHT = 900
    screen_help = pygame.display.set_mode((WIDHT, HEIGHT))

    buttons_size = (201, 93)
    exit_button = pygame.Surface(buttons_size)
    exit_button = pygame.image.load("image/exit_button.png").convert()
    exit_button.set_colorkey((255, 255, 255), RLEACCEL)
    exit_button_rect = exit_button.get_rect()
    exit_button_rect = exit_button_rect.move((200, 780)) 

    pygame.display.set_caption("SortIt help")
    background = pygame.image.load("image/help_img.png").convert()
    running = True
    while running:
        if pygame.mouse.get_pressed()[0] == 1:
            
            if ((exit_button_rect.right > pygame.mouse.get_pos()[0] > exit_button_rect.left)
                    and (exit_button_rect.top < pygame.mouse.get_pos()[1] < exit_button_rect.bottom)):
                    running = False
                    
        screen_help.blit(background, [0,0])
        screen_help.blit(exit_button, [200,780])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                   running = False
        pygame.display.flip()           

    pygame.quit()
