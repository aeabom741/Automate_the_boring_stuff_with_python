while True:
    print("Who are you?")
    name = input()
    if name != 'Joe':
        continue
    print("Hello Joe, What is the password?")
    password = input('password:')
    if password == 'password':
        break
print('Access')