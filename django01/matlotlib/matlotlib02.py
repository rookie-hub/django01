# import matplotlib.pyplot as plt
# print(plt.style.available) # 查看可使用的图表样式
# ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
import matplotlib.pyplot as plt
suq = [1,4,9,16,25] # 图表需要的数据
input_values = [1,2,3,4,5]

plt.style.use('bmh') # 使用内置的图表样式

fig,ax = plt.subplots() # 这个函数可以在一张图中绘制多个图表
# fig就是整张图片 ， ax就是多个图表



ax.plot(input_values,suq,   # 线条的数据来源
        linewidth=3, # 线条宽度
        color='red', # 线条颜色
        #linestyle='--', # 线型
        #dash_capstyle='round', # 每个虚线小段的形状，round为圆角矩形
        alpha=0.9,      # 透明度
        ) # 绘制图表

ax.set_title('平方数',fontsize=24) # 设置图表名称和名称字体大小
ax.set_xlabel('值',fontsize=14) # 设置X轴名称和名称字体大小
ax.set_ylabel('值的平方',fontsize=14) # 设置y轴名称和名称字体大小

# plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['font.sans-serif']=['KaiTi'] #显示中文标签



# 设置刻度标记的大小
ax.tick_params(axis='both',labelsize=14)


plt.show() # 查看图表