
import os
from PIL import Image
#import matplotlib.pyplot as plt

flowe_classes = ['daisy','dandelion','roses','sunflowers','tulips','Nymphaea',
                 'Tropaeolum_majus','Digitalis_purpurea','peach_blossom','Jasminum','Matthiola',
                 'Rosa','Rhododendron','Dianthus','Cerasus','Narcissus','Pharbitis','Gazania',
                 'Eschscholtzia','Tithonia'] 


for name in flowe_classes:
    a = os.listdir('D:/PyCharm 2020.2/PycharmProjects/flower/data/'+name)
    count = 1
    print(name)
    for x in a:
        #print(x)
        
        img=Image.open('D:/PyCharm 2020.2/PycharmProjects/flower/data/'+name+'/'+x)
        dst=img.transpose(Image.FLIP_LEFT_RIGHT)#左右互换
        newname='D:/PyCharm 2020.2/PycharmProjects/flower/data/'+name+'/'+name+'_'+str(count)+'.jpg'
        dst=dst.convert('RGB')
        dst.save(newname)
        count += 1
    print('complete')
