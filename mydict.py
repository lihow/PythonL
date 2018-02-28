class Dict(dict):
	'''
	Simple dict but also support access as x.y style
	>>> d1 = Dict()
	>>> d1['x'] = 100
	>>> d1.x
	100
	>>> d1.y = 200
	>>> d1['y']
	200
	>>> d2 = Dict(a=1, b=2, c='3')
	>>> d2.c
	'3'
	'''
	def __init__(self, **kw):
		#super().__init__(**kw)
		super(Dict, self).__init__(**kw)
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
	def __setattr__(self, key, value):
		self[key] = value
		
#以下内容为文档测试用
if __name__ == '__main__':
	import doctest
	doctest.testmod()