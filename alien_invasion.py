import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为分类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Diana_Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """游戏主循环"""
        while True:
            self._check_event()
            self._update_screen()

            # 显示绘制屏幕
            pygame.display.flip()

    def _check_event(self):
        """ 监视键鼠事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """循环绘制"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()


if __name__ == '__main__':
    # 创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()
