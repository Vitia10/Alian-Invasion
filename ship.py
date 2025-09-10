import pygame as pg
class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pg.image.load('images/ship3.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False 
        self.moving_down = False
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.rect.x = self.x 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed  
        if self.moving_up and self.rect.top > 0:
            self.rect.y -=1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y +=1 
        self.rect.x = self.x       
       
        


