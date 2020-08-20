allGuests = {'Alice':{'apple':5,"pretzels": 12},
             'Bob':{'ham sandwiches':3,'apple':2},
             'Carol':{'cap':3,"apple pie":1}
             }

def total(person,objects):
    number = 0
    for i, j in person.items():
        number += j.get(objects,0)
    return number


print('Number of thing being brought')
print('-Apple      ' + str(total(allGuests,'apple')))
print('-cap        ' + str(total(allGuests,'cap')))
print('-apple pie  ' + str(total(allGuests,'apple pie')))