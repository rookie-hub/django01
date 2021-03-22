import pygame
class Ship:
    def __init__(self,ai_game): # 传入AlienInvasion类的实例
        ''' 初始化飞船并设置初始值'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()



        # 加载飞船图形并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() # 飞船的外接矩形


        # 对于新飞船都将其放在屏幕的底部中央位置
        self.rect.midbottom = self.screen_rect.midbottom

        # 右移动标志
        self.moving_right = False
        # 左移动标志
        self.moving_left = False

        # 获取游戏的参数设置对象
        self.setting = ai_game.settings
        # 设置飞船属性X中可以存储浮点数
        self.x = float(self.rect.x)  # 飞船的外接矩形的X轴坐标
        #print("x==",self.x)

    def blitme(self):
        ''' 在指定位置处绘制飞船'''
        self.screen.blit(self.image,self.rect)


    # 在pygame中，原点(0,0)位于屏幕的左上角，行右下方移动时坐标值将增大，右下角的坐标就是(1200,800),这些坐标对应的是游戏窗口，不是物理屏幕

    def update(self):
        '''根据移动标志记录飞船的位置'''
        # 更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed

        if self.moving_left and self.rect.left > 0 :
            self.x -= self.setting.ship_speed

        # 根据self.x更新rect对象
        self.rect.x = self.x

    def ship_center(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)




















