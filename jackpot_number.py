import random 

random.randint(1,100)

jackpot = random.randint(1,100)
count = 1
guess = int(input('Abey ooo , Chal Guess Kar : '))

while guess != jackpot :
    count += 1
    if guess < jackpot:
        print('Guess Higher : ')
    else:
        print('Guess Lower : ')
    
    guess = int(input('Galat hai Fir Se Guess Kar : '))
    
print('Sahi Jwab : Ye leh tera 7 peti ')

print('Calculation loading.......')

print('Aapne sahi jawab dene me lgaye pure ',count , 'attempt' )

