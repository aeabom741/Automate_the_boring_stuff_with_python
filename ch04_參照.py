spam = 42
cheese = spam
spam = 100
print(cheese)
print(spam)

spam = [0,1,2,3,4,5]
cheese = spam
print(cheese)
print(spam)
print('---------------')
spam[0] = 1
print(cheese)

#傳入參照
def eggs(someParameter):
    someParameter.append('Hello')
    
spam = [1,2,3]
eggs(spam)
print(spam)
print('----------------')
#copy模組的copy()和deepcopy()函式
import copy

spam = ["A","B","C","D"]
chesses = copy.copy(spam)
chesses[1] = "G"
print(spam)
print(chesses)