import  pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''单个外星人的类'''
    def __init__(self,ai_game):
        '''初始化参数并设置初始位置'''
        super().__init__()
        self.screen = ai_game

        # 加载外星人图形并设置其rect值
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect() # 外星人的外接矩形

        # 外星人的初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)

        # 外星人的设置
        self.settings = ai_game.settings

    def check_edges(self):
        '''如果即将越界就返回True'''
        screen_rect = self.screen.screen.get_rect()  # 获取屏幕的矩形
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        '''移动外星人'''

        self.x += (self.settings.alien_speed * self.settings.fleet_direction) # 水平位置，右移是+1，左移是-1
        self.rect.x = self.x



