# coding=utf-8
import random

def hello():
	print 'hello'
def helloWithName(name):
	print 'hello ' + str(name)

hello()
helloWithName('chengyan')
helloWithName(10086)
helloWithName('成焱')

def AskAnswer(number):
	if number == 1:
		return '确定'
	elif number == 2:
		return '决定是这样'
	elif number == 3:
		return '是的'
	elif number == 4:
		return '稍后再试'
	elif number == 5:
		return '再试'
	elif number == 6:
		return '稍后再问问'
	elif number == 7:
		return '我的回答是No'
	elif number == 8:
		return '很糟糕'
	elif number == 9:
		return '很怀疑'
raninta = random.randint(1,9)
reply = AskAnswer(raninta)
print(reply)
print('dog','cat','animal')