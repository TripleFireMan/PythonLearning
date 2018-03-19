#! /usr/local/bin/python3
# python3 编码输出问题 http://blog.csdn.net/houzhiguo/article/details/55259490
# pw.py 密码管理箱

import sys
import io
import pyperclip

# 给标准输出设置编码
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

PassWords = {'sina':'3526871',
			 'neteast':'chengyandinglei',
			 'alibaba':'chengyan_mayun'}

if len(sys.argv) < 2:
	print('Usage:python pw.py[account] - copy account password')
	sys.exit()
account = sys.argv[1]

if account in PassWords:
	pyperclip.copy(PassWords[account])	
	print('PassWord for ' + account + ' has copied to clipboard')
else:
	print('there is no account named ' + account)