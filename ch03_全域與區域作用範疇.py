def spam():
    eggs = 3133
    print(eggs)
spam()
print('-----------')
def spam():
    egg = 99
    bacon()
    print(egg)

def bacon():
    ham = 101
    egg = 0
    print(egg)    
spam()
bacon()
print('--------------')
def spam():
    print(egg)
egg = 42
spam()
print(egg)
print('--------------')

def spam():
    egg = 'spam local'
    print(egg)

def bacon():
    egg = 'bacon local'
    print(egg)
    spam()
    print(egg)
    
eggs = 'global'
bacon()
print(eggs)