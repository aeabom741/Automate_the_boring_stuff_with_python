#不使用正規法尋找文
def foundnumber(number):
    if len(number) != 12:
        return False
    for i in range(0,4):
        if not number[i].isdecimal():
            return False
    if number[4] != '-':
        return False
    for i in range(5,8):
        if not number[i].isdecimal():
            return False
    if number[8] != '-':
        return False
    for i in range(9,12):
        if not number[i].isdecimal():
            return False
    return True

number = '0903-004-838'

print(foundnumber(number))

message = 'Call me 0903-004-838 if you have anything to need'

for i in range(len(message)):
    chunk = message[i:i+12]
    if foundnumber(chunk):
        print("The phone number is:" + chunk)