import pygame
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg = pygame.image.load("images/back.jpg")
        self.ship_speed = 1.3
        self.bullet_speed = 0.9
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255,255,255)
