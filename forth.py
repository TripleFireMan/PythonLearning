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