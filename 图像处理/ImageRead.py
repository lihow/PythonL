# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:13:44 2017

@author: Lenovo
"""

import matplotlib.pyplot as plt
import tensorflow as tf

#读取图像的原始数据
image_raw_data=tf.gfile.FastGFile("C:/Users/Lenovo/Desktop/cat.jpg",'rb').read()

with tf.Session() as sess:
    #tf.image.decode_png函数对png格式的图像进行解码，解码的结果为一张量，在使用它之前需要明确调用运行过程
    img_data=tf.image.decode_jpeg(image_raw_data)
    #输出解码之后的三维矩阵
    #print(img_data.eval())
    #使用pyplot工具可视化得到的图像
    plt.imshow(img_data.eval())
    plt.show()
    
    resized=tf.image.resize_images(img_data,[300,300],method=0)
    print(img_data.get_shape())
    plt.imshow(resized.eval())
    plt.show()
   
    '''
    #将数据的类型转化为实数方便下面的样例程序对图像进行处理
    img_data=tf.image.convert_image_dtype(img_data,dtype=tf.uint16)
    
    encoded_img=tf.image.encode_jpeg(img_data)
    with tf.gfile.GFile("C:/Users/Lenovo/Desktop/2.jpg",'wb') as f:
        f.write(encoded_img.eval())
    '''
    