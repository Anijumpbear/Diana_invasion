import pygame

class Ship:
    """飞船类"""

    def __init__(self, ai_game):
        """位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        """图形"""
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        """初始位置"""
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """绘制"""
        self.screen.blit(self.image, self.rect)
