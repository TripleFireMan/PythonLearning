#encoding=utf-8


while True:
	print('输入你的年龄:')
	age = raw_input()
	if age.isalnum():
		break
	print('年龄必须是数字')

while True:
	print('输入你的密码:')
	password = raw_input()
	if password.isalpha():
		break
	print('密码只能是字母和数字')