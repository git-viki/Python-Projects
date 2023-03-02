import random

num = random.randint(1,100)
print(num)

guess = int(input('enter the guessing number :'))

if guess == num :
    print(' wow, You are Guessing right number : ')
elif guess < num :
    print(' number is less than your guess : ')
elif guess > num :
    print('number is greter than  your guess :')
