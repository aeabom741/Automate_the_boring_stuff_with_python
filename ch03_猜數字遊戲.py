import random
secret = random.randint(1,10)
print("I'm thinking of number between 1 and 20")

for guesstime in range(1,7):
    guessnumber = int(input("Your guess number:"))
    
    if guessnumber > secret:
        print('Too high')
        print('Guess time ' + str(6 - guesstime))
    elif guessnumber < secret:
        print('Too low')
        print('Guess time ' + str(6 - guesstime))
    else:
        break
if secret == guessnumber:
    print("Good job you are guess in " + str(guesstime) + ' times')
else:
    print("The answer is " + str(secret))