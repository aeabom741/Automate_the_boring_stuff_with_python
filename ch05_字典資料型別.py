mycat = {'size':'fat','color':'gray','disposition':'loud'}
print(mycat['size'])
print("My cat has "+ mycat['color'] +' fur' )
#字典與串列
#字典沒有順序性
spam = ['cats','dogs','moose']
bacon = ['dog','moose','cats']
print(spam == bacon)

eggs = {"name":"Zophie","species":"cat","age":"8"}
ham = {"species":"cat",'name':"Zophie",'age':'8'}
print(eggs == ham)

birthday = {'Alice':'Apr 1',"Bob":'Dec 12',"Carol":"Mar 4"}

while True:
    name = input("Please enter name to know this person birthday:")
    if name == '':
        break
    if name in birthday:
        print(birthday[name] + " is " + name + ' birthday')
    else:
        print(name + " is not in this information")
        print('please updata the information')
        birthday[name] = input("His birthday is:")
        print('Information is updata')
        
#Key()、value()和item()方法
spam = {'color':'red','age':42}
for i,j in spam.items():
    print(i,j)

print(spam.keys())
print(lisr(spam.keys()))