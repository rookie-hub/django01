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

