class Set:
    def __init__(self):
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 设置飞船速度
        self.ship_speed = 1.5

        self.bullet_speed = 1.0 # 子弹速度
        self.bullet_width = 3 # 子弹宽度
        self.bullet_heigth = 15 # 子弹高度
        self.bullet_color = (60,60,60) # 子弹颜色为灰色
        self.bullet_allowed = 3 # 子弹数量