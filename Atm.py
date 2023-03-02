class Atm:
    
    # constructer  - it is a special function -> superpower
    def __init__(self):
        self.pin = ''
        self.blance = 0
        # print('MAin to execute ho gya')
        self.menu()
    def menu(self):
        User_input = input("""
        Hii How can i help you ?
        1. Press 1 to creat pin
        2. Press 2 to chnage pin
        3. Press 3 to check balance 
        4. Press 4 to withdraw 
        5. Anythings else to exit 
            _   
        : """)
        
        if User_input == '1':
            #creat pin
            self.Create_pin()
        elif User_input == '2':
            # change pin
            self.Change_pin()
        elif User_input == '3':
            # check balance 
            self.Check_balance()
            
        elif User_input == '4':
            # withdraw
            self.Withdraw_balance()
        else:
            exit(' Exit Sucessfully  ')
    
    def Create_pin(self):
        user_pin = int(input('Enter your pin :'))
        self.pin = user_pin
        
        user_balance = int(input('enter balance : '))
        self.balance = user_balance
        
        print('pin created successfully')
        self.menu()
        
    def Change_pin(self):
        old_pin = int(input('Enter your old pin'))
        
        if old_pin == self.pin:
            #let him change the pin
            new_pin = int(input(' Enter new pin : '))
            if new_pin == self.pin:
                print('This is same as your old pin')
            self.pin == new_pin
            
            print('Pin changed successfully')
        
        else:
            print('Nai krne de skta re baba ')
        self.menu()
        
    def Check_balance(self):
        user_pin = int(input('Enter your pin : '))
        if self.pin == user_pin:
            print('Your Balance is ', self.balance)
        else:
            print('Chal nikal yha se ')
        self.menu() 
          
    def Withdraw_balance(self):
        user_pin = int(input('Enter your pin :'))
        if user_pin == self.pin:
            amount = int(input('Enter Money Do you Want to Withdraw : '))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('Waiting...')
                print('Withdraw sucessfully ', amount, 'your available balance is ', self.balance)

            else:
                print('Tera Baap yaha se chhor ke gya tha ya teri maa')
            self.menu()
        else:
            print('Abey yeh sahi pin Daal : ')       
        self.menu()     
        
obj = Atm()
# print(type(obj))

