#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
import os
def Print_File(files):
    print(x for x in files)
def Find_File(files, name):
    return [x for x in files if x.find(name) != -1]
def Find_folder(folder,name):
    #os.chdir(folder)
    dirnames = [x for x in os.listdir('.') if os.path.isdir(x)]
    #Print_File(dirnames)
    filenames = [x for x in os.listdir('.') if os.path.isfile(x)]
    #result_file = []
    if len(filenames):#
        result_file = [x for x in filenames if x.find(name) != -1]
    #Print_File(result_file)
    result_folder = []
    if len(dirnames):#
        for dirname in dirnames:
            result_tmp = Find_folder(dirname, name)
            result_folder.extend(result_tmp)
        #Print_File(result_folder)
    result_file = result_file.extend(result_folder)
    result = []
    for r in result_file:
        result.append(os.path.join(folder, r))
    #os.chdir('..')
    return result
        

dirnames = [x for x in os.listdir('.') if os.path.isdir(x)]
filenames = [x for x in os.listdir('.') if os.path.isfile(x)]
for dirname in dirnames:
    print('enter folder: ' + dirname)

for x in Find_File(filenames, 'my'):
    print(x)

#Find_folder('.', 'my')