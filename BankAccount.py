# Create a Python class called BankAccount which represents a bank account, having as attributes: 
# accountNumber, name , balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a deposit() method which manages the deposit actions. 
# (deposit() method will take parameter d and you will increase the balance with the amount d)
# Create a withdrawal() method which manages withdrawals actions. 
# (withdrawal() method will take parameter w, you will reduce the amount of balance with w,
# if w is larger than the balance: then print Impossible operation! Insufficient balance!")
# Create a bankFees() method to apply the bank fees with a percentage of 5% of the balance account. 
# (When this method is called, the balance amount should reduce 5%)
# Create a display() method to display account details.
class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self,d):
        self.balance = self.balance+d

    def withdrawal(self,w):
        if w < self.balance:
            self.balance = self.balance-w
        else:
            print('Impossible operation! Insufficient balance!')

    def bankFees(self):
        self.balance = self.balance*0.95
        
    def display(self):
        print('Account Number is',self.accountNumber)
        print('Account Owner is',self.name)
        print('Account Balance is',self.balance,'$')

newAccount = BankAccount(5562325,'Mary Jones',4750)
BankAccount.display(newAccount)
newAccount.deposit(50)
BankAccount.display(newAccount)
newAccount.withdrawal(250)
BankAccount.display(newAccount)
newAccount.withdrawal(8500)
BankAccount.display(newAccount)
newAccount.bankFees()
BankAccount.display(newAccount)



