# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 12:29:07 2017

@author: Lenovo
"""

from PIL import Image

img= Image.open('C:/Users/Lenovo/Desktop/li.jpg')
img.show()

out = img.transpose(Image.FLIP_LEFT_RIGHT)
#实现镜像翻转
out.show()
out.save("C:/Users/Lenovo/Desktop/li2.jpg")