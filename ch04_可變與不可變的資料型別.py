name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)

eggs = [1,2,3]
eggs = [4,5,6]
print(eggs)

egg = [1,2,3]
del egg[2]
del egg[1]
del egg[0]

egg.append(4)
egg.append(5)
egg.append(6)
print(egg)

#多元組資料型別
eggs = ("hello",42,0.5)
print(eggs[0])
print(eggs[1])
print(eggs[:])

#使用list()和tuple()函式來轉換型別
a = tuple(['cat','dog',5])
print(a)
a = list(a)
print(a)
a = list('hello')
print(a)