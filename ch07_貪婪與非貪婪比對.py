import re
"""
貪婪與非貪婪比對
"""

haRegex = re.compile(r'(ha){3,5}')
mo1 = haRegex.search("hahahahaha")
print(mo1.group())

nongreedyRegex = re.compile(r'(ha){3,5}?')
mo2 = nongreedyRegex.search("hahahahaha")
print(mo2.group())

print('--------------------------------')
print('--------------------------------')
"""
findall()方法
"""
phoneRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
mo1 = phoneRegex.findall('Work:0903-004-838,Home:0921-099-286')
print(mo1)

print('--------------------------------')
print('--------------------------------')
"""
字元分類
"""
xmasRegex = re.compile(r'\d+\s\w+')
mo1 =  xmasRegex.findall("12 Leo, 11 Kelon, 10 Simon, 9 Wei")
print(mo1)

print('--------------------------------')
print('--------------------------------')
"""
建立屬於自己的字元分類
"""
viewRegex = re.compile(r'[AEIOUaeiou]')
mo1 = viewRegex.findall('Robocop eats baby food')
print(mo1)

#加入^尋找相反的字
contextReget = re.compile(r'[^AEIOUaeiou]')
mo1 = contextReget.findall('Robocop eat baby food ,BABY FOOD')
print(mo1)
"""
^字元和$字元
"""
begingRegex = re.compile(r'^hello')
mo1 = begingRegex.search('hello world')
print(mo1)

endRegex = re.compile(r'hello$')
mo2 = endRegex.search('hello word')
print(mo2 is None)

mo3 = endRegex.search("world hello")
print(mo3)

wholestringisnum = re.compile(r'^\d+$')
mo1 = wholestringisnum.search('0532188664')
print(mo1)

"""
萬用字元
"""
atRegex = re.compile(r'.at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat')
print(mo1)












