import pygame
import os
from scripts.game import Game
class App:
    def __init__(self):
        self.fps = 60
        self.scena = pygame.display.set_mode((480, 720))
        self.time = pygame.time.Clock()
        self.running = True
        pygame.display.set_caption('DudleJump')
        image = pygame.image.load(os.path.join('assets','icons','icon.ico'))
        pygame.display.set_icon(image)
        self.game = Game()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):
        ...
    def render(self):
        self.scena.fill((0, 0, 0))
        self.game.render_objects(self.scena)
        pygame.display.update()
    



    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

            self.time.tick(self.fps)

    