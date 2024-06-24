
from random import randint
import pygame
from scripts.functions import load_image
from scripts.platform import Platform, MovingPlatform
from scripts.constants import CreatePlatformEvent, display_size
class PlatformGenerator:
    def __init__(self, step):
        self.step = step
    def create_start_configuration(self):
        platform = Platform(
            load_image('assets', 'images', 'platform.png'),
            [display_size[0] / 2, display_size[1] - 50]
        )
        event = pygame.Event(CreatePlatformEvent, {'platform': platform})
        pygame.event.post(event)
        for y in range(display_size[1], 0, -self.step):
            self.create_platform(y)
    def create_platform(self, center_y):
        r = randint(0, 100)

        if r > 77:
            image = load_image('assets', 'images', 'moving-platform.png')
        else:
            image = load_image('assets', 'images', 'platform.png')

        
        width = image.get_width()
        center_x = randint(width // 2, display_size[0] - width // 2)
        if r > 77:
            speed = randint(10, 100) / 10
            platform = MovingPlatform(image, [center_x, center_y], speed)
        else:   
            platform = Platform(image, [center_x, center_y])
        event = pygame.Event(CreatePlatformEvent, {'platform': platform})
        pygame.event.post(event)
    def update(self, offset_y, platforms):
        if platforms and platforms[-1].rect.centery - offset_y >= self.step:
            self.create_platform(offset_y)
            platforms.remove(platforms[0])
        