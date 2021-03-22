from random import choice
# choice() 方法，参数1是一个列表/元祖等等，参数2为从列表中一次随机取出的个数，
# 参数3为是否可以重复获取元素，为True时，会获取到重复元素;参数4是一个一维数组，制定了每个元素被获取的概率，默认为None，表示概率一致；
# random.choice([1,2,3,4,5], 1, replace=False, p=[0.1, 0, 0.3, 0.6, 0])
class RandomWalk:
    def __init__(self,num=5000):
        self.num = num # 随机漫步的次数

        # 所有的随机都起始于(0,0),使用两个列表来存储每一次随机点的x,y坐标
        self.x = [0,]
        self.y = [0,]

    def fill_walk(self): # 确定每次随机漫步生成的点和其方向
        '''计算漫步包含的所有点'''

        # 不断进行随机漫步，知道漫步的次数大于指定的漫步次数
        while len(self.x) < self.num:
            # 决定散点x轴的方向
            x_direction = choice([-1,1])
            # 决定散点x轴方向的距离
            x_distance = choice([0,1,2,3,4])
            # 最新随机漫步的点距离上一个点的X坐标
            x_step = x_direction * x_distance

            # 决定散点y轴的方向
            y_direction = choice([-1, 1])
            # 决定散点y轴方向的距离
            y_distance = choice([0, 1, 2, 3, 4])
            # 最新随机漫步的点距离上一个点的Y坐标
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 最新随机漫步点的位置
            x_con = self.x[-1] + x_step
            y_con = self.y[-1] + y_step

            # 将最新的漫步点添加到x,y列表中
            self.x.append(x_con)
            self.y.append(y_con)





