#! usr/local/bin/python3
 
import sys
import pyperclip
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

source = 'list1 today is sunday\nlist2 tomorrow is cloudy\nlist3 yestody is rainy'

# 拷贝 并不会返回任何值
pyperclip.copy(source)
copyed = pyperclip.paste()
print(copyed)
# 分割并加星号
lines = copyed.split('\n')
for i in range(0,len(lines)):
	lines[i] = '*' + lines[i]
copyed = '\n'.join(lines)
pyperclip.copy(copyed)	
# 粘贴到剪切板
pyperclip.paste()



