"""

字串方法

"""

print('upper()、lower()、isupper()和islower()等字串方法')
spam = "hello world!"
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)
"""
print("How are you")
feeling = input('Talk:')
if feeling.lower() == 'great':
    print('I\'m great too')
else:
    print("OK sorry")
"""
print('-----------------------')
print('-----------------------')
print('isX字串方法')
print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('123654'.isdecimal())
print('This Is A Title 123'.istitle())
print('-----------------------')
print('-----------------------')
"""
while True:
    print("Enter your age:")
    age = input("Your age:")
    if age.isdecimal():
        break
    else:
        print("Please enter nuber:")

while True:
    print('Please selection password number')
    password = input('Your password:')
    if password.isalnum():
        print("Password is already")
        break
    else:
        print("Only can type letters and numbers")
"""        
print('-----------------------')
print('-----------------------')
print("startwith()和endswith()字串方法")
print('Hello world'.startswith("Hello"))
print("Hello world".endswith("world"))
print("abcd123".startswith("abc"))
print("abcd123".endswith('5'))
print('-----------------------')
print('-----------------------')
print('join()和split()字串方法')
print(','.join(['cat','rat','dog']))
print(' '.join(['My','name','is','Leo']))
print('ABC'.join(["My",'Name','Is','Simon']))
print('My name is Simpon'.split())
print("MyABCNameABCIsABCSimon".split("ABC"))

spam = '''Dear Alice
How have you been? I am fine
There is a container in the fridge
that is labeled "Mike Experiment".

please do not drink it.
Sincerely
Bob
'''
spam = spam.split('\n')
print(spam) 
print('-----------------------')
print('-----------------------')
print("使用rjust(),ljust(),和center()方法對其文字")
print('Hello world'.rjust(20))
print("Hello world".ljust(20))
print('Hello'.rjust(20,'*'))
print('Hello'.ljust(20,'-'))
print('Hello'.center(20,'+'))
def printobject(item,left,right):
    print("PICNIC ITEMS".center(left + right))
    print('-----------------'.center(left + right))
    for i , j in item.items():
        print(i.ljust(left,'.') + str(j).rjust(right))
    print('-----------------'.center(left + right))
items = {"Apple": 5 ,'Sandwich' : 9 ,'Pie':2}
printobject(items,15,5)
print('-----------------------')
print('-----------------------')
print("使用strip(),rstrip()和lstrip()刪除空白字元")
spam = '    Hello world     '
print(spam.strip())
print(spam.lstrip())
print('-----------------------')
print('-----------------------')
print("使用pyperclip模組複製與貼上字串")
import pyperclip
pyperclip.copy('Hello world')
print(pyperclip.paste())


        