import re

text = 'My phone number is 0903-004-838'

foundnumber =  re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
mo = foundnumber.search(text)
print(mo.group())

