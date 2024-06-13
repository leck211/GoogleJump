
from scripts.sprite import Sprite
import pygame
from scripts.functions import load_image
from scripts.player import Player
class Game:
    def __init__(self):
        self.background = load_image('assets','images','background.png')
        self.platforms = [
            Sprite(load_image('assets','images','background.png'))
        ]
        self.player = Player(
            load_image('assets','images','player.png'),
            (240, 600),
            5,
            15,
            0.75,
        )
    def process_key_down_event(self, key):
        if key == pygame.K_a:
            self.player.is_walking_left = True
        if key == pygame.K_d:
            self.player.is_walking_right = False
    def process_key_up_event(self, key):
        if key == pygame.K_a:
            self.player.is_walking_left = False
        if key == pygame.K_d:
            self.player.is_walking_right = False
    def update_objects(self):
        self.player.update()





    def render_objects(self, scena):
        scena.blit(self.background, (0, 0))
        for platform in self.platforms:
            platform.render(scena)
        self.player.render(scena)