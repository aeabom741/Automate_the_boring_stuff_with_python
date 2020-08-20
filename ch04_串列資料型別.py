spam = ['cat','bat','rat','elephone']
print(spam[0])
print(spam[1])

print('Hello ' + spam[2])
print("The " + spam[0] + ' eat the '+ spam[2])
print('-----------------------------------------')
spam = [['cat','bat'] , [10,20,30,40]]
print(spam[0])
print(spam[1])

print(spam[0][1])
print(spam[1][2])
print('-----------------------------------------')
#負索引值
spam = ['cat','bat','rat','elephone']
print(spam[-1])
print(spam[-3])
print('The ' + spam[-1] + ' afraid of ' + spam[-2])
print('-----------------------------------------')
#使用切片取得子串列
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print(spam[:2])
print(spam[:])
print('-----------------------------------------')
#使用len()取得串列得長度
print(len(spam))

print('-----------------------------------------')
#使用索引足標改變串列的值
spam = ['cat','bat','rat','elephone']
spam[1] = 'aasdfwr'
spam[2] = spam[1]
print(spam)
print('-----------------------------------------')
#串列的連接和複製
a = [1,2,3] + ['A','B','C']
print(a)
b = ['A','B','C'] * 3
print(b)
spam = [1,2,3]
spam = spam + ["A",'B','C']
print(spam)
#使用del陳述句刪除串列中的值
spam = ['cat','bat','rat','elephone']
del spam[2]
print(spam)

