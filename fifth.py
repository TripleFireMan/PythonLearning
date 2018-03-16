#encoding=utf-8

mycat = {'size':'fat','color':'gray','dispostion':'loud'}

print('mycat size:' + mycat['size'])
print('mycat has ' + mycat['color'] + ' flur.')

spam = {12345:'luggage combination',42:'the answer'}
spam.setdefault('color','blue')
print spam['color']

print spam.keys()
print spam.values()
print spam.items()

# 利用多重赋值技巧获取到key与value
for key,value in spam.items():
	print('key : ' + str(key) + ' value : ' +  str(value))

# in spam 相当于 in spam.keys()
for item in spam:
	print item

for value in spam.values():
	print value

# 检查字典中是否存在键或值
if 'color' in spam:
	print('name in')
else:
	print('name not in')

if 'the answer' in spam.values():
	print('the answer in')

# get方法获取字典中的某个key对应的value，如果获取失败，采用第二个参数值
print('get factory '+spam.get('factory','milk'))

# setdefault 给字典设置一个默认值，当不存在值的时候设置
# 第一次不存在时设置成功
spam.setdefault('sex','boy')
print(spam)
# 第二次已经存在时设置不生效
spam.setdefault('sex','girl')
print(spam)


allGuests = {'alice':{'apple':5,'pretzels':12},
			 'bob':{'ham sandwiches':3,'apple':2},
			 'carol':{'cups':3,'apple pies':1}}
def totalBrought(guests,item):
	total = 0
	for items in guests.values():
		total+=items.get(item,0)
	return total

print('Numbers of things being brought:')
print(' - apples ' + str(totalBrought(allGuests,'apple')))
print(' - cups ' + str(totalBrought(allGuests,'cups')))
print(' - cakes ' + str(totalBrought(allGuests,'cakes')))
print(' - pretzels ' + str(totalBrought(allGuests,'pretzels')))














