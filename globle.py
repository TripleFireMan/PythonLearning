#coding=utf-8

def namelocal():
	egg = '鸡蛋'
	print egg

def namegloble():
	global egg 
	egg = '鸡皮疙瘩'
	print egg

egg = 'egg'
# print egg
namelocal()
namegloble()
print egg
