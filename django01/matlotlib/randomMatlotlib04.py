import matplotlib.pyplot as plt
from django01.matlotlib.RandomWalk import RandomWalk as rw

rs = rw() # 创建随机漫步实例
rs.fill_walk() # 调用随机漫步方法获取所有漫步点坐标组成的x,y列表

# 使用plot将漫步实例中的x,y列表的数据绘制出来
plt.style.use('classic') # 内置图表模板
fig,ax = plt.subplots() # 这个函数可以在一张图中绘制多个图表
# fig就是整张图片 ， ax就是多个图表


point_number = range(rs.num)
ax.scatter(rs.x,rs.y,c=point_number,cmap=plt.cm.Reds,s=20,edgecolors='none') # 绘制散点图

# 突出起点和终点
ax.scatter(0,0,c='green',s=100,edgecolors='none') # 绘制散点图
ax.scatter(rs.x[-1],rs.y[-1],c='blue',s=100,edgecolors='none') # 绘制散点图


# ax.axis([0,5000,0,5000]) # 随机漫步不要设置过大的坐标轴取值范围

plt.show()

