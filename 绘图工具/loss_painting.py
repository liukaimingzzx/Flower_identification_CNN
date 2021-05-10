import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
list1 = []
list2 = []
list3 = []
list4 = []
f = open("D:\PyCharm 2020.2\PycharmProjects\\flower\save\\alexnet_acc.txt","r")
f1= open("D:\PyCharm 2020.2\PycharmProjects\\flower\save\\AlexNet_loss.txt","r")
for line in f.readlines():
    line=line.strip('\n')
    list1.append(int(line.split(',')[0]))
    list2.append(float(line.split(',')[1]))
for line in f1.readlines():
    line=line.strip('\n')
    list3.append(int(line.split(',')[0]))
    list4.append(float(line.split(',')[1]))
x1 = list1
y1 = list2
x2 = list3[0:200]
y2 = list4[0:200]

fig = plt.figure(figsize = (9,6))       #figsize是图片的大小`
ax1 = fig.add_subplot(1, 1, 1) # ax1是子图的名字`
# ‘’g‘’代表“green”,表示画出的曲线是绿色，“-”代表画的曲线是实线，可自行选择，label代表的是图例的名称，一般要在名称前面加一个u，如果名称是中文，会显示不出来，目前还不知道怎么解决。
p2 = pl.plot(x1, y1,'b-', label = u'AlexNet(batch_size=100)')
pl.legend()
#p3 = pl.plot(x2,y2, 'r-', label = u'AlexNet(batch_size=100)')
#pl.legend()
pl.xlabel(u'epoch')
pl.ylabel(u'acc(%)')
plt.rcParams['font.sans-serif']=['SimHei']
plt.title('AlexNet(batch=100)准确率变化曲线')
#x7=[0,0.5,1.0,1.5,2.0,2.5,3.0]
#plt.yticks(x7)
print(list1)
print(list2)
# plot the box
#tx0 = 95
#tx1 = 105
#设置想放大区域的横坐标范围
#ty0 = 0.00
#ty1 = 0.3
#设置想放大区域的纵坐标范围
#sx = [tx0,tx1,tx1,tx0,tx0]
#sy = [ty0,ty0,ty1,ty1,ty0]
#pl.plot(sx,sy,"purple")
#axins = inset_axes(ax1, width=1.5, height=1.5, loc='right')
#loc是设置小图的放置位置，可以有"lower left,lower right,upper right,upper left,upper #,center,center left,right,center right,lower center,center"
#axins.plot(x1,y1 , color='red', ls='-')
#axins.axis([95,105,0.0,0.3])
plt.savefig("train_results_loss.png")
plt.show()


