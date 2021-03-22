import matplotlib.pyplot as plt

# 散点的数据来源
# x_value = [1,2,3,4,5]
x_value = range(1,101)
# y_value = [1,4,9,16,25]
y_value = [x**2 for x in x_value]


plt.style.use('Solarize_Light2') # 使用内置的图表样式
fig,ax = plt.subplots() # 这个函数可以在一张图中绘制多个图表
# fig就是整张图片 ， ax就是多个图表
ax.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,s=10) # 绘制散点图
ax.axis([0,110,0,11000]) # 设置坐标轴的取值范围

ax.set_title('平方数',fontsize=24) # 设置图表名称和名称字体大小
ax.set_xlabel('值',fontsize=14) # 设置X轴名称和名称字体大小
ax.set_ylabel('值的平方',fontsize=14) # 设置y轴名称和名称字体大小

plt.rcParams['font.sans-serif']=['KaiTi'] #显示中文标签

# 设置刻度标记的大小
ax.tick_params(axis='both',which='major',labelsize=14)

plt.show()
# plt.savefig('squares_plot.png',bbox_inches='tight')
