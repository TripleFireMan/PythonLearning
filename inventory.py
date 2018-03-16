#encoding=utf-8

stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':6}
def displayInventory(inventory):
	print('inventory:')
	total = 0
	for key,value in inventory.items():
		print(str(value)+' ' + key)
		total += value
	print('totla number of items: ' + str(total))
displayInventory(stuff)

# 添加物品到背包
def addToInventory(inventory,addedItems):
	for obj in addedItems:
		inventory.setdefault(obj,0)
		for key,value in inventory.items():
			if obj == key:
				print(obj+'----------')
				inventory[key] += 1	
	return inventory

				

dragLoot = ['gold coin','dagger','gold coin','gold coin','ruby']

updated = addToInventory(stuff,dragLoot)

displayInventory(updated)
