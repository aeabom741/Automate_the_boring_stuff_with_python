'''
原有字串項目新增項目符號
'''

import pyperclip

text = """List of animal
List of aquarium life
List of cultivars
List of biologists"""

pyperclip.copy(text)
lines = pyperclip.paste().split('\n')


#將字串分割成串列 利用足標前頭加星號
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
print(pyperclip.paste())
