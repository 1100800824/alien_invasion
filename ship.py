import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.moving_right = False
        self.moving_left = False
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load(r'D:\pythonlearning\alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
    
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        self.center = float(self.rect.centerx)
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left == True and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center