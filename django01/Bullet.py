import  pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_game):
        '''在当前的飞船位置创建一个子弹对象'''
        super().__init__()
        self.screen =ai_game.screen # 窗口对象
        self.settings = ai_game.settings # 游戏中的参数对象
        # 现在(0,0)的位置设置一个子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_heigth)
        self.rect.midtop = ai_game.ship.rect.midtop # 子弹顶部的初始位置为飞船的顶部位置

        # 用小数存储子弹的位置
        self.y = float(self.rect.y)
        # 子弹颜色
        self.color = self.settings.bullet_color


    # 射击的方法本质就是将子弹的y坐标值较小向0靠近
    def update(self):

        # 坐上坐标为0,0  那么子弹越向上走其y值就越小，所以是减去移动距离
        self.y -= self.settings.bullet_speed
        # 更新子弹位置
        self.rect.y = self.y

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)
