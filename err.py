'''
#8.错误处理 调用栈示例代码
def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s) * 2
def main():
	bar('0')
main()
'''
import logging
import pdb
logging.basicConfig(level=logging.INFO)
s = '0'
pdb.set_trace()
n = int(s)
logging.info('n = %d' % n)
print(10 / n)