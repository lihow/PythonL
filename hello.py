# _*_ coding: utf-8 _*_
'a test module'
__author__ = 'Michael Liao'
import sys

class Hello(object):
	def hello(self, name='world'):
		print('Hello, %s.' % name)
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
	
'''
第1行是标准注释，第行注释表示.py文件本身使用标准UTF-8编码  
第2行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
第3行使用_ _author_ _变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名
'''