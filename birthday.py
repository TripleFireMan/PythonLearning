#encoding=utf-8

birthdays = {'alice':'Apr 1','bob':'Des 12','carol':'Mar 4'}

while True:
	print('enter a name:(blank to quite)')
	name = raw_input()
	if name == '':
		break
	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('I donot have birthday information for ' + name)
		print('What is their birthday:')
		bday = raw_input()
		birthdays[name] = bday
		print('birthday database updated')
