import pprint
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
    print("Keys:" + i + ' Value ' + str(j))
print('-----------------------------')
print(spam.keys())
print(list(spam.keys()))
#檢查字典中鍵與值是否存在
spam = {'name':'Zophie',"age":'7'}
print('name' in spam.keys())
print('7' in spam.values())
#get()用法
picnicItems = {'apple':5,'cups':2}
print("I'm brining "+str(picnicItems.get('apple',0)) +  ' cups')
print("I'm brining "+str(picnicItems.get('egg',0)) +  ' cups')

#setdefault()方法
spam = {'name':'Pooka','age':5}
spam.setdefault('color','black')
print(spam)

messages = "It was a bright cold day in April"
count = {}
for character in messages:
    count.setdefault(character,0)
    count[character] += 1
pprint.pprint(count)






