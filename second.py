#coding=utf-8

import sys
import string
import io


print(round(2.768,2))
print('hello')
print '百草枯千万不能碰'

# if elif else 语句
name = 'chengy2an'
age = 10

if name == 'chengyan':
	print '123'
	print '11-'
elif age == 10:
	print 'age == 10'
else:
	print '456' + 'good'
	print 'good'


# while 语句

spam = 0

if spam < 5:
	spam = spam + 1
	print 'spam = ' + str(spam) 

while  spam < 5:
	spam += 1
	print 'spam = ' + str(spam) 

yourname = ''

inputname = ''
while not inputname:
	print 'please input name'
	inputname = str(raw_input()) 
	if inputname == '':
		continue
	print 'please input your guests count'
	numberofGuest = int(raw_input())
	if numberofGuest == 0:
		print 'no guests did input'
	else:
		print('be sure to have enough room for ' + str(numberofGuest) + ' guests.')
print 'done'





















