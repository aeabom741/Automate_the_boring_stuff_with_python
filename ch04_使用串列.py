name = []
while True:
    print("The number " + str(len(name) +1) + ' cat nam')
    catname = input("Please enter the cat name:")
    if catname == '':
        break
    name.append(catname)
    
print('The cat are:')
for cat in name:
    print(cat)
    