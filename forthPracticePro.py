import random

def appendListThenPrint(list):
	result = ''
	for obj in list:
		result += str(obj)
		if list.index(obj) != len(list) - 1:
			result += ', '	
		if list.index(obj) == len(list) -2:
			result += 'and '
	return result

spam = ['apples','bananas','tofub','cats']

result = appendListThenPrint(spam)

print result

grid = [['.','.','.','.','.','.'],
		['.','0','0','.','.','.'],
		['0','0','0','0','.','.'],
		['0','0','0','0','0','.'],
		['.','0','0','0','0','0'],
		['0','0','0','0','0','.'],
		['0','0','0','0','.','.'],
		['.','0','0','.','.','.'],
		['.','.','.','.','.','.'],
		]

xlen = len(grid)
ylen = len(grid[0])

for x in xrange(0,ylen):
	end = 'start'
	for y in xrange(0,xlen):
		if end == 'end':
			print grid[y][x]
		else:
			print grid[y][x],
		if y == xlen-2:
			end = 'end'
	