# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 16:18:38 2017

@author: Lenovo
"""
import os
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#生成整数型的属性
def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

#生成字符串型的数据
def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

#cwd='C:/Users/Lenovo/Desktop/手写数字/digit/'
cwd='C:/Users/Lenovo/Desktop/temp/train/'
classes={'0','1','2','3','4','5','6','7','8','9'}

#输出TFRecord的文件位置
filename='C:/Users/Lenovo/Desktop/temp/train/digit.tfrecords'
#创建一个writer来写TFRcord文件
writer=tf.python_io.TFRecordWriter(filename)

for index,name in enumerate(classes):
    class_path=cwd+name+'/'
    for img_name in os.listdir(class_path):
        img_path=class_path+img_name #每一个图片的地址
        print(img_path)
        img=Image.open(img_path)
        w, h = img.size
        print('Original image size: %sx%s' % (w, h))
        #img=img.resize((128.128))
        img_raw=img.tobytes()#将图片转化为二进制格式
        example = tf.train.Example(features=tf.train.Features(feature={
            "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[index])),
            'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw]))
        })) #example对象对label和image数据进行封装
        '''
        example=tf.train.Example(features=tf.train.Feature(feature={
                'label':_int64_feature(index),
                'img_raw':_bytes_feature(img_raw)}))
        '''
        writer.write(example.SerializeToString())#序列化为字符串
writer.close()