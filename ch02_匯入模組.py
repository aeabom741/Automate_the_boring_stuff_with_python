import random
import sys
for i in range(5):
    print(random.randint(1,10))
    
while True:
    print('Type exit to exit')
    response = input("Type:")
    if response == 'exit':
        sys.exit()
    print("You type "+ response)