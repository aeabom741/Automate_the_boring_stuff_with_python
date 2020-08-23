import re

"""
利用括弧來分組
"""

text = 'The phone number is 0903-004-838'
foundnumber = re.compile(r'(\d\d\d\d)-(\d\d\d)-(\d\d\d)')
mo = foundnumber.search(text)

print(mo.group(1))
print(mo.group(2))
print(mo.groups())

print('--------------------------------')
print('--------------------------------')
"""
使用'|'比對多個分組
"""

heroRegex = re.compile(r'Batman|Tina')
mo1 = heroRegex.search("Batman and Tina")
print(mo1.group())

mo2 = heroRegex.search('Tina and Batman')
print(mo2.group())


batRegex = re.compile(r'Bat(man|mobile|bat|copter)')
mo = batRegex.search('Batmobile loss a wheel')
print(mo.group())

print('--------------------------------')
print('--------------------------------')
"""
使用'?'作為可選擇性比對
"""

print("使用'?'作為可選擇性比對")
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventure of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventure of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d\d)-\d\d\d-\d\d\d')
mo = phoneRegex.search('The phone number is 0903-004-838')
print(mo.group(1))

print('--------------------------------')
print('--------------------------------')
"""
使用星號比對符合零次或多次
"""

woRegex = re.compile(r'Bat(wo)*man')
mo1 = woRegex.search('The advanture of Batwoman')
print(mo1.group())

mo2 = woRegex.search("The advanture of Batman")
print(mo2.group())

mo3 = woRegex.search("The advanture of Batwowowowowowoman")
print(mo3.group())

print('--------------------------------')
print('--------------------------------')
"""
使用加號比對符合一次或多次
"""
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search("The advanture of Batman")
print(mo1 is None)

mo2 = batRegex.search("The advanture of Batwowowowowowoman")
print(mo2.group())

mo3 = batRegex.search('The advanture of Batwoman')
print(mo3.group())

print('--------------------------------')
print('--------------------------------')
"""
使用大括弧指定比對次數
"""

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search("HaHaHa")
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2 is None)
