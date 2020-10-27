from PIL import Image
import numpy as np
#为了定义好俯视角el、方位角az与深度，将三个变量定义在前面便于调节
el=np.pi/2.2
az=np.pi/4.
dep=90.
#转化为灰度图
im=Image.open("im.jpg")
im=im.convert('L')
im.save('灰度.jpg')
#取梯度，对图像进行重构
a=np.asarray(im).astype('float')
grd=np.gradient(a)
grd_x,grd_y=grd
grd_x=grd_x*dep/100.
grd_y=grd_y*dep/100.
#制造光源效果
dx=np.cos(el)*np.cos(az)
dy=np.cos(el)*np.sin(az)
dz=np.sin(el)
uni_x=grd_x
uni_y=grd_y
uni_z=1
b=255*(dx*uni_x+dy*uni_y+dz*uni_z)
b=b.clip(0,255)
im0=Image.fromarray(b.astype('uint8'))
im0.save('im0.jpg')