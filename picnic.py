#encoding=utf-8
def printpicnic(itemsDics,leftWidth,rightWidth):
	print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))
	for k,v in itemsDics.items():
		print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))

picnicitems = {'sandwiches':4,'apples':12,'cups':4,'cookies':8000}

printpicnic(picnicitems,12,5)

printpicnic(picnicitems,20,6)