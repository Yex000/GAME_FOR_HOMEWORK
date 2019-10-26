import pygame
import random
from main import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    speed_player
)

class NUMBER(pygame.sprite.Sprite):
    def __init__(self):
        super(NUMBER, self).__init__()
        """self.image = pygame.image.load("jet.png").convert()
        self.image.set_colorkey((0, 100, 200), RLEACCEL)"""
        self.surf = pygame.Surface((40, 40))
        self.surf.fill((0, 100, 200))
        self.rect = self.surf.get_rect(
            center=(
                random.ranint(20, SCREEN_WIDTH-20), -50
                   )
        )
    def update(self):
        self.rect.move_ip(speed_player, 0)
        if self.rect.bottom < SCREEN_HEIGHT:
            self.kill()