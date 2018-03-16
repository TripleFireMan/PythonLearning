#encoding=utf-8

# 没有单引号
string = 'this is a single string with no quotes'
print string
# 用双引号包起来的字符串内可以使用单引号
stringwithquotes = "this is a single string with ' quotes"
print stringwithquotes
# 转义字符
stringUseConvert = 'this is a single string with convert \' string'
print stringUseConvert
# 常见的转义字符还有 \t : 制表符, \n : 换行符,\\ : 倒斜杠
stringDemos = 'Hello there!\nHow are you?\nI\'m doing fine.'
print stringDemos
# r 开头会使字符串忽略转义字符，按照原字符输出
stringRaw = r'That is Carol\'s cat'
print stringRaw
# 多行字符串，以三个单引号，或三个双引号开头,忽略所有的单双引号、换行制表符
stringForMutilLine = '''stringForMutilLine
						instring ‘’‘’“”“‘’‘’‘’‘’‘ 
						djfkdjkj jkdjskjksjdsuwuwuuwulajkkj;;
							'''
print stringForMutilLine

"""
以三个双引号或者单引号开头的注释，称之为多行注释
"""