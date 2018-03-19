# -*- coding: utf-8 -*-

import pyperclip
import sys
import unicodedata

# 没有单引号
string = 'this is a single string with no quotes'
print(string)
# 用双引号包起来的字符串内可以使用单引号
stringwithquotes = "this is a single string with ' quotes"
print(stringwithquotes)
# 转义字符
stringUseConvert = 'this is a single string with convert \' string'
print(stringUseConvert)
# 常见的转义字符还有 \t : 制表符, \n : 换行符,\\ : 倒斜杠
stringDemos = 'Hello there!\nHow are you?\nI\'m doing fine.'
print(stringDemos)
# r 开头会使字符串忽略转义字符，按照原字符输出
stringRaw = r'That is Carol\'s cat'
print(stringRaw)
# 多行字符串，以三个单引号，或三个双引号开头,忽略所有的单双引号、换行制表符
stringForMutilLine = '''stringForMutilLine
						instring ‘’‘’“”“‘’‘’‘’‘’‘ 
						djfkdjkj jkdjskjksjdsuwuwuuwulajkkj;;
							'''
# print(stringForMutilLine)

"""
以三个双引号或者单引号开头的注释，称之为多行注释
"""

# 字符串切片
spam = 'Hello World!'

print(spam[:5])
print(spam[6:])
print(spam[0])
print(spam[11])
print(spam[-1])

# 字符串的in or not in
print('Hello' in 'Hello World')
print('HELLO' in 'Hello World')
print('wawa' not in 'Hello World')

# upper()、lower()
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

# islower()、isupper()
newspam = 'abc123'
print(newspam.islower())
print(newspam.isupper())

# 其他的字符串方法 
print(newspam.isalpha())
print(newspam.isalnum())
print(newspam.isspace())
print(newspam.istitle())

# startswith() endswith()
print('Hello World'.startswith('Helle'))
print('Hello World'.endswith('World'))

# join() split()
animals = ['cat','dog','pig']
animalsstr = '.'.join(animals)
print(animalsstr)
animalsplit = 'cat tiger chicken cow deer'
print(animalsplit.split(' '))

# 文本对齐 ljust()、rjust(),center()
hello = 'Hello World'
print(hello.rjust(20,'='))
print(hello.ljust(20,'*'))
print(hello.center(20,'+'))

# 删除字符串
spam = '   Hello World  '
print(spam)
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
# 会删除首尾俩端的'Sapm','mapS','Spam'等组合，顺序不重要，
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam)
spam = spam.strip('ampS')
print(spam)

copyed = pyperclip.paste().encode('ascii','ignore').decode('ascii')
print(copyed)







