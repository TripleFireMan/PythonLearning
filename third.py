name = 10

try:
	div = name / 0
except Exception, e:
	print e
	print Exception
	print('hehe')
# else:
# 	print('else')
# finally:
# 	print('finally')