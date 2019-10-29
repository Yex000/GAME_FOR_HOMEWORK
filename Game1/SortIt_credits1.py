import pygame
from pygame.locals import(
    RLEACCEL
    )

def credits_fn():
    ''' show credits window'''

   
    pygame.init()

    # Window parameters
    WIDHT = 612
    HEIGHT = 900
    screen_credits = pygame.display.set_mode((WIDHT, HEIGHT))

    buttons_size = (201, 93)# Exit button settings
    exit_button = pygame.Surface(buttons_size)
    exit_button = pygame.image.load("image/exit_button.png").convert()
    exit_button.set_colorkey((255, 255, 255), RLEACCEL)
    exit_button_rect = exit_button.get_rect()
    exit_button_rect = exit_button_rect.move((200, 780)) 

    pygame.display.set_caption("SortIt credits")
    background = pygame.image.load("image/credits_img.png").convert() # Background for Credits
    running = True
    while running:
        if pygame.mouse.get_pressed()[0] == 1:
            
            if ((exit_button_rect.right > pygame.mouse.get_pos()[0] > exit_button_rect.left)
                    and (exit_button_rect.top < pygame.mouse.get_pos()[1] < exit_button_rect.bottom)):# Is the exit button pressed?
                    running = False
                    
        # Adding background and button             
        screen_credits.blit(background, [0,0])
        screen_credits.blit(exit_button, [200,780])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                   running = False
        pygame.display.flip() # Updating the display           

    #pygame.quit()   
