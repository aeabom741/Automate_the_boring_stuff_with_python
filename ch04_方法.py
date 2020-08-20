#使用index()方法搜尋串列的值
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))
print(spam.index('heyas'))

#使用append()和insert()方法新增值到串列中
spam = ['cat', 'dog' ,'bat']
spam.append('moose')

spam.insert(1,'chicken')
print(spam)

#使用remove()方法刪除串列中的值
spam = ['cat','bat','rat','elephant']
spam.remove('cat')
print(spam)

spam = ['cat','bat','rat','cat','hat','cat']
spam.remove('cat')
print(spam)

#使用sort()方法對串列中的值進行排序
spam = [2,5,3.14,1,-7]
spam.sort()
print(spam)
spam = [2,5,3.14,1,-7]
spam.sort(reverse = True)
print(spam)

spam = ["Alice", "ants", "Bob", "badgers", "Carol", "cats"]
spam.sort()
print(spam)
spam = ['a','z','A','Z']
spam.sort()
print(spam)