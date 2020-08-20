for i in range(4):
    print(i)
    
supplies = ['pens','staplers','flame-throwers','binder']
for i in range(len(supplies)):
    print('Index ' +str(i) + ' in supplies is ' + supplies[i] )
    
#in和not in 運算子
mypet = ['Zophie','Pooka','Fat-tail']
print("Enter a name:")
name = input('name:')
if name not in mypet:
    print("I do not have pet name: " + name)
else:
    print(name + ' is my pet')
    
#多重指定值的ˊ技巧
cat = ['fat','orange','loud']
size,color,disposition = cat
print(cat)
print(size)
print(color)
print('-----------------')
a,b = 'Alice' , 'Bob'
a,b = b ,a
print(a)
print(b)
