print('轉義字元')
spam = 'say hi ti Bob\'s mother'
print(spam)
print("Hello there\nHow are you\nI'm doing fine")
print('----------------------')
print("----------------------")
print('原始字串')
print(r'That is Carol\'s cat')
print('----------------------')
print("----------------------")
print('使用三重引號的多行字串')
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion
Sincerely,
Bob''')
print('----------------------')
print("----------------------")
print("多行註釋")
"""
This is a test Python Program
Written by Sweight al@inventwithpython.com
This program was designse for Python3
"""
def spam():
    """
    This is a multiline comment to help
    explain what the spam() function does.
    """
    print("Hello")
spam()

print("----------------------")
print("----------------------")
print('字串的足標與切片')
spam = 'Hello world!'
print(spam[0])
print(spam[4])
print(spam[0:5])
print(spam[:5])
print(spam[6:11])
print("----------------------")
print("----------------------")
print('字串的in和not in 運算子')
print('Hello' in 'Hello world')
print('HELLO' in 'hello world')
print(' ' in spam)



