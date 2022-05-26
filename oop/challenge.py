class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'Account Owner: {self.owner}\n Account Balance: ${self.balance}'
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal accepted')
        else:
            print('Funds unavailable!')