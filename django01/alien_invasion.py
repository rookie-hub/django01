import sys
import pygame
from django01.ship import Ship
from django01.set import Set
from django01.Bullet import Bullet
from django01.alien import Alien
from time import sleep
from django01.game_stats import GameStats

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

        self.aliens = pygame.sprite.Group() # 存储外星人的编组方法
        self._create_fleet()

        # 用于存储游戏统计信息的实例
        self.stats = GameStats(self)

    def _check_alients_bottom(self):
        '''检测是否有外星人到达底部'''
        screen_rect = self.screen.get_rect() # 获取屏幕矩形
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        '''飞船被外星人撞击后，飞船数-1，清空子弹和外星人，重置飞船位置，重新生成一群外星人'''
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1 # 飞船数-1
        else:
            self.stats.game_active = False

        # 清空子弹和外星人
        self.aliens.empty()
        self.bullets.empty()

        # 重置飞船位置，重新生成一群外星人
        self._create_fleet()
        self.ship.ship_center()

        # 暂停
        sleep(0.5)




    def _create_fleet(self):
        '''创建一群外星人'''
        alient = Alien(self) # 生成一个外星人并获取其数据来计算一行可以容纳多少个外星人
        alien_width,alien_height = alient.rect.size # 外星人所占的宽度和高度,size属性包含一个元祖
        available_space_x = self.settings.screen_width - (2 * alien_width) # 可用于放置外星人的水平宽度
        number_aliens_x = available_space_x // ( 2 * alien_width) # 返回不大于结果的一个最大的整数 ， 可在水平宽度生成外星人的数量

        # 可用的垂直宽度
        ship_height = self.ship.rect.height # 飞船的高度
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        # 可生成的外星人的行数
        number_rows = available_space_y // (2 * alien_height)

        # 创建外星人群
        for row_number in range(number_rows):
            for alient_number in range(number_aliens_x):
                # 创建一个外星人并将其加入当前行
                self._create_alien(alient_number,row_number) # 两个参数是用于计算外星人初始x,y坐标

    def _create_alien(self,alient_number,row_number):
        '''创建一个外星人并放在当前行'''
        alien = Alien(self)
        alien_width,alient_height = alien.rect.size # 单个外星人的宽度
        alien.x = alien_width + 2 * alien_width * alient_number # 当前外星人的宽度起始坐标
        alien.rect.x = alien.x # 将外星人的宽度坐标赋值给外星人矩形的宽度坐标
        alien.rect.y = alien.rect.height + 2 * row_number * alien.rect.height
        self.aliens.add(alien) # 将外星人添加到外星人列表


        #self.aliens.add(alien) # 将生成的外星人实例对象添加到列表中

    def _check_fleet_edges(self):
        '''遍历外星人列表查看是否有外星人到达屏幕边缘'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._chang_fleet_direction()
                break


    def _chang_fleet_direction(self):
        '''将外星人下移并将移动方向更改,整个外星人的下移和更改'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed # 向下移动
        # 反方向移动
        self.settings.fleet_direction *= -1


    def run_game(self):
        '''开始游戏的循环'''
        while 1:
            # 监视键盘和鼠标事件
            self._check_events()
            if self.stats.game_active:
                # 飞船的移动
                self.ship.update()

                # 子弹的移动
                self._update_bullets()

                # 外星人的位置更新，需要在子弹之后，判断子弹移动后是否击中了外星人
                self._update_aliens()
            # else:
            #     sys.exit()

            # 更新屏幕
            self._update_screen()

    def _update_aliens(self):

        '''更新列表中所有外星人的位置'''
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()

        self._check_alients_bottom()


    def _update_bullets(self):
        # 更新子弹的位置
        # 为bullets列表中每一个子弹调用Bullet类的update方法来更新子弹的y值
        self.bullets.update()
        for bullet in self.bullets.copy():
            # 删除子弹
            if bullet.y <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
        # 检查子弹是否和外星人的rect发生了碰撞
        self._check_bullet_alient_collision()



    def _check_bullet_alient_collision(self):
        '''响应子弹和外星人碰撞'''
        # 删除发生碰撞的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        # pygame中sprite.groupcollide可以检测两个列表的rect是否发生了碰撞
        # 参数1 发生碰撞的列表1
        # 参数2 发生碰撞的列表2
        # 参数3 为True，那么发生碰撞时删除当前列表1中的当前发生碰撞的子弹，为False那么子弹击中外星人后子弹不会消失
        # 参数4 为True，那么发生碰撞时删除当前列表2中的当前发生碰撞的外星人
        if not self.aliens:
            # 如果外星人消灭完了，就消除子弹并重新创建一群外星人
            self.bullets.empty()  # 清空子弹列表
            self._create_fleet()



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

        self.aliens.draw(self.screen) # 绘制aliens列表中所有的外星人

        # 让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并允许它
    ai = AlienInvasion()
    ai.run_game()