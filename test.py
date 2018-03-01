#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
import os
def Find_File(files, name):
    return [x for x in files if x.find(name) != -1]
dirnames = [x for x in os.listdir('.') if os.path.isdir(x)]
filenames = [x for x in os.listdir('.') if os.path.isfile(x)]
for dirname in dirnames:
    print('enter folder: ' + dirname)

for x in Find_File(filenames, 'my'):
    print(x)
'''
for filename in filenames:
    if filename.find('my') != -1:
        print(filename)
'''