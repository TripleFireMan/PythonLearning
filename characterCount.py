#encoding=utf-8
import pprint
message = 'it was a bright cold day in april,and the clocks striking thirteen.'
count = {}

for character in message:
	count.setdefault(character,0)
	count[character] = count[character] + 1
prettystring = pprint.pformat(count)
pprint.pprint(count)
print prettystring