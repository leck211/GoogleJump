



from cgitb import text
from scripts.platform_generator import PlatformGenerator
import pygame
from scripts.functions import load_image, get_path
from scripts.player import Player
from scripts.constants import display_size
class Game:
    def __init__(self):
        self.background = load_image('assets','images','background.png')
        self.platforms = []
        self.player = Player(
            load_image('assets','images','player.png'),
            (240, 600),
            5,
            22,
            0.75,
        )
        self.offset_y = 0
        self.platform_generator = PlatformGenerator(200)
        self.platform_generator.create_start_configuration()
        self.font = pygame.Font(get_path('assets', 'fonts', 'pixel.ttf'), 32)
        self.score = 0
        self.losed = False

        pygame.mixer.music.load(get_path('assets', 'music', 'caves.mp3'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)



        
    def process_key_down_event(self, key):
        if self.losed:
            self.losed = False
            self.offset_y = 0
            self.score = 0
            self.platforms = []

            self.platform_generator.create_start_configuration()
            self.player.reset((240, 600))

        elif key == pygame.K_a:
            self.player.is_walking_left = True
        elif key == pygame.K_d:
            self.player.is_walking_right = True
    def process_key_up_event(self, key):
        if key == pygame.K_a:
            self.player.is_walking_left = False
        if key == pygame.K_d:
            self.player.is_walking_right = False
    def render_objects(self, scena):
        scena.blit(self.background, (0, 0))
        for platform in self.platforms:
            platform.render(scena, self.offset_y)
        self.player.render(scena, self.offset_y)
        if self.losed:
            score_text = self.font.render(
                'Ваш счёт: ' + str(self.score), True, (0, 0, 0)
            )
            hint_text = self.font.render(
                'Нажмите любую клавишу', True, (0, 0, 0)
            )
            text_rect = score_text.get_rect(
                centerx = display_size[0] / 2,
                centery = display_size[1] / 2 - 25,
            )
            hint_rect = hint_text.get_rect(
                centerx = display_size[0] / 2,
                centery = display_size[1] / 2 + 25,
            )
            scena.blit(score_text, text_rect)
            scena.blit(hint_text, hint_rect)
        else:
            text_image = self.font.render(str(self.score), True, (0, 0 , 0))
            text_rect = text_image.get_rect(centerx = display_size[0] / 2, top = 10)
            scena.blit(text_image, text_rect)
    def update_objects(self):
        for platform in self.platforms:
            platform.update()
            if self.player.collide(platform.rect):
                self.player.on_platform = True
        self.player.update()
        if self.player.rect.bottom - self.offset_y < display_size[1] / 3:
            self.offset_y = self.player.rect.bottom - display_size[1] / 3
            self.score = abs(round(self.offset_y / 10))
        self.platform_generator.update(self.offset_y, self.platforms)
        self.losed = self.player.rect.top - self.offset_y >= display_size[1]
        if self.losed:
            return