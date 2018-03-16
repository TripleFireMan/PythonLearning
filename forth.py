#encoding=utf-8
print [1,2,3]
spam = ['cat',1,'dog']

# 负数下标
print spam[-1]
# 切片数组
print spam[1:3]

# 省略第一个切片下标,相当于从0开始
print spam[:2]
# 省略第二个切片下标，相当于直到结束
print spam[1:]
# 可以使用负数下标进行切片
print spam[0:-2]
# len函数求取列表长度
print len(spam)
# 修改下标值
spam[0] = 'pig'
print spam
# 列表添加 和复制
spam = spam + ['tiger']
print spam
spam = spam * 3
print spam
# del函数删除值
del(spam[0])
del spam[0]
print spam

# 判断一个值是否在列表中
if 'pig' in spam:
	print 'boy in spam'
else:
	print 'boy not in spam'

# 多重赋值
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = spam
print(c1+c2+c3+str(c4)+c5)

# index方法查找值,如果值在列表中就会返回该值，如果值不在列表中，会报错。且如果值在列表中，会返回第一次出现时的下标
searchSpam = spam.index(1)
print searchSpam

# append增加值
spam.append('blue')
print spam

# insert插入值
spam.insert(1,'chicken')
print spam

# remove 移除值
spam.remove('pig')
print spam

# sort 排序
spam.sort()
print spam
# sort 逆序
spam.sort(reverse=True)
print spam

# 字符串
strname = 'blue'
for x in strname:
	print x
print strname[-2]
print strname[0:2]
print strname[2:]

# 元组[不可变] 和 列表[可变]
tuble = ('name','age',10, 10.99)

print tuble

type = type(('name',))
print type
print type('2222')

# list和tuple函数转换类型
obj1 = [1,2,3]
obj2 = (4,5,6)

print obj1
print obj2

obj3 = tuple(obj1)
obj4 = list(obj2)

print obj3
print obj4

print obj1
print obj2


#copy 与 deepCopy,copy只拷贝一层，deepcopy会拷贝多层


















