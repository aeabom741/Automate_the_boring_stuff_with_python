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

