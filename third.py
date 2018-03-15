#encoding=utf-8

import math

def collatz(number):
	if number % 2 == 0:
		print(number // 2)
		return number // 2
	else:
		print(3 * number + 1)
		return 3 * number + 1


try:
	print('请输入:')
	inputNumber = int(raw_input())	
	print('你输入了 ' + str(inputNumber))
	value = collatz(inputNumber)
	print('运算结果为:' + str(value))
	while value != 1:
		value = collatz(value)
		print('运算结果为:' + str(value))
	finNumber = value
except Exception, e:
	print('你必须输入一个整数')


	