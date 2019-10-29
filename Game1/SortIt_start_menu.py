import pygame
import SortIt_open_main, SortIt_help1, SortIt_credits1
from pygame.locals import(
    RLEACCEL
    )
pygame.init()
pygame.mixer.init()

WIDHT = 612
HEIGHT = 900
screen = pygame.display.set_mode((WIDHT, HEIGHT))

pygame.display.set_caption("SortIt")
background = pygame.image.load("image/start_game_bgr1.png").convert()

buttons_size = (201, 93)

play_button = pygame.Surface(buttons_size)
play_button = pygame.image.load("image/play_button.png").convert()
play_button.set_colorkey((255, 255, 255), RLEACCEL)
play_button_rect = play_button.get_rect()
play_button_rect = play_button_rect.move((200, 100))

help_button = pygame.Surface(buttons_size)
help_button = pygame.image.load("image/help_button.png").convert()
help_button.set_colorkey((255, 255, 255), RLEACCEL)
help_button_rect = help_button.get_rect()
help_button_rect = help_button_rect.move((200, 240))

credits_button = pygame.Surface(buttons_size)
credits_button = pygame.image.load("image/credits_button.png").convert()
credits_button.set_colorkey((255, 255, 255), RLEACCEL)
credits_button_rect = credits_button.get_rect()
credits_button_rect = credits_button_rect.move((200, 380))

exit_button = pygame.Surface(buttons_size)
exit_button = pygame.image.load("image/exit_button.png").convert()
exit_button.set_colorkey((255, 255, 255), RLEACCEL)
exit_button_rect = exit_button.get_rect()
exit_button_rect = exit_button_rect.move((200, 520))

pygame.mixer.music.load("morning.mp3")
pygame.mixer.music.play(loops=-1)

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if pygame.mouse.get_pressed()[0] == 1:
            
            if ((play_button_rect.right > pygame.mouse.get_pos()[0] > play_button_rect.left)
                and (play_button_rect.top < pygame.mouse.get_pos()[1] < play_button_rect.bottom)):
                running = False
                SortIt_open_main.open_main()
                pygame.quit()

            elif ((help_button_rect.right > pygame.mouse.get_pos()[0] > help_button_rect.left)
                and (help_button_rect.top < pygame.mouse.get_pos()[1] < help_button_rect.bottom)):
                SortIt_help1.help_fn()
                
            elif ((credits_button_rect.right > pygame.mouse.get_pos()[0] > credits_button_rect.left)
                and (credits_button_rect.top < pygame.mouse.get_pos()[1] < credits_button_rect.bottom)):
                SortIt_credits1.credits_fn()

            elif ((exit_button_rect.right > pygame.mouse.get_pos()[0] > exit_button_rect.left)
                and (exit_button_rect.top < pygame.mouse.get_pos()[1] < exit_button_rect.bottom)):
                running = False

    screen.fill((255, 255, 255))

    screen.blit(background, [0,0])
    screen.blit(play_button, [200,100])
    screen.blit(help_button, [200,240])
    screen.blit(credits_button, [200,380])
    screen.blit(exit_button, [200,520])
    pygame.display.flip()
    
    pygame.time.delay(25)
       
    pygame.display.flip()
