# Email Validation In python (Using String Functions)

email = input('Enter your Email id : ') #g@g.in , sudovicky@gmail.com
k ,j , d = 0 , 0 , 0
if len(email) >= 6 :
    if email[0].isalpha():
        if ('@' in email) and (email.count('@')==1):
            if (email[-4]== ".") ^ (email[-3]== "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper(): # w-- w == w
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == '_' or i == '.' or i == '@':
                        continue
                    else:
                        d = 1 

                if k == 1 or j == 1 or d == 1:
                    print('Invalid email : 5')
            else:
                print('Invalid email 4')

        else:
            print('invalid email. 3')

    else:
        print('invalid email 2')
else :
    print('Invalid email 1 ')

password = input('Enter your Password : ')
print('wait for a sec...')
print('Loading........')
print('Yes , Now You are all set !! ')