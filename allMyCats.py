#encoding=utf-8

# print('请输入猫1:')
# cat1 = raw_input()
# print('请输入猫2:')
# cat2 = raw_input()
# print('请输入猫3:')
# cat3 = raw_input()
# print('请输入猫4:')
# cat4 = raw_input()
# print('请输入猫5:')
# cat5 = raw_input()
# print('请输入猫6:')
# cat6 = raw_input()

# print('猫们：')
# print(cat1 + ' ' + cat2 + ' ' + cat3 + ' ' + cat4 + ' ' + cat5 + ' ' + cat6)

cats = []

while True:
	print('请输入猫' + str(len(cats) + 1) + ':')
	catname = raw_input()
	if catname == '':
		 break
	cats += [catname]

print('猫们:')
for x in xrange(0,len(cats)):
	print cats[x]

print('请输入你要查找的猫的名字:')
searchedCatName = raw_input()
if searchedCatName in cats:
	print('你要找的猫在')
else:
	print('你要找的猫不在')

mimi,moxi,luxifa = cats


print('mimi:'+ mimi)
print('moxi:'+ moxi)
print('luxifa:'+ luxifa)




