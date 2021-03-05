import sys
import pygame
from django01.ship import Ship
from django01.set import Set
from django01.Bullet import Bullet

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并初始化资源'''
        pygame.init()

        self.settings = Set()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # 创建显示窗口
        #self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)  # 创建一个覆盖整个显示器的窗口
        # 无法预知显示器的屏幕尺寸，所以在窗口后更新这些参数
        #self.settings.screen_width = self.screen.get_rect().width # 设置游戏参数类的宽度参数
        #self.settings.screen_height = self.screen.get_rect().height # 设置游戏参数类的高度参数
        pygame.display.set_caption("外星人入侵 ")  # 显示窗口的名称

        # 设置背景色
        self.bg_color = self.settings.bg_color  # 浅灰色
        # 255,0,0 表示红色
        # 0,255,0 表示绿色
        # 0,0,255 表示蓝色

        # 第一步 添加飞船实例,并将当前AlienInvasion实例作为参数传入
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group() # 这个对象类似于列表，可以管理发射出去的子弹

    def run_game(self):
        '''开始游戏的循环'''
        while 1:
            # 监视键盘和鼠标事件
            self._check_events()

            # 飞船的移动
            self.ship.update()

            self._update_bullets()


            # 更新屏幕
            self._update_screen()

    def _update_bullets(self):
        # 更新子弹的位置
        # 为bullets列表中每一个子弹调用Bullet类的update方法来更新子弹的y值
        self.bullets.update()
        for bullet in self.bullets.copy():
            # 删除子弹
            if bullet.y <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _check_events(self):
        # 响应键盘和鼠标事件
        for event in pygame.event.get():
            #print("键盘中的事件===",event.type)
            #print("键盘中右箭头的事件",pygame.K_RIGHT)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: # 监测键盘按下事件pygame.KEYDOWN
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP :
                self._check_keyup_events(event)


    def _check_keydown_events(self,event):
        '''响应键盘按下事件'''
        if event.key == pygame.K_RIGHT:  # 监测到发生了键盘按下事件并且这个事件是右箭头事件就执行以下代码
            #("向右移动一格")
            # 向右移动飞船一个单位
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE: # 键盘按下事件并且按键为空格键的时候发射子弹
            self._first_ullet()


    def _first_ullet(self):
        ''' 创造一颗子弹并加入当前bullets列表中'''
        if len(self.bullets) < self.settings.bullet_allowed :
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        '''响应键盘弹起事件'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        '''更新屏幕上的图像，并切换到新屏幕'''
        # 每次循环时都重新绘制屏幕
        self.screen.fill(self.bg_color)

        # 第二步 调用飞船的blitme方法来绘制指定位置的飞船
        self.ship.blitme()

        # 绘制每一颗子弹的位置
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并允许它
    ai = AlienInvasion()
    ai.run_game()