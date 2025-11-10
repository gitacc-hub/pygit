"""
Simulate a simple banking system where customers can open accounts, deposit, withdraw, and check balances. 
Use an abstract Account class for common features.
"""
from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self,acc_number):
        self.acc_number=acc_number
        self.balance=0
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def check_balance(self):
        pass
class BankAccount(Account):
    def deposit(self,amount):
        self.balance+=amount
        return f"Deposited:{amount} ,Balance:{self.balance}"
    def withdraw(self,amount):
        if self.balance>=amount:
           self.balance-=amount
           return f"Withdrew- ${amount} ,Balance:${self.balance}"
    def check_balance(self):
        if self.balance >=0:
            return f"Balance: ${self.balance}"
        else:
            return "Insufficient funds"

class User:
    def __init__(self,name):
        self.name=name
        self.accounts=[]
    def create_account(self,account):
        self.accounts.append(account)
        return f"Account {account.acc_number}created for {self.name}"
    def show_accounts(self):
        print(f"\n{self.name}`s Accounts:\n")
        for acc in self.accounts:
            print(f"Account No: {acc.acc_number}, Balance:{acc.balance}")

acc1=BankAccount(1234)
acc2=BankAccount(2345)
user1=User("Abdirahman")
user1.create_account(acc1)
user1.create_account(acc2)

#Deposit money to the accounts
acc1.deposit(100000)
acc2.deposit(100000)
#Withdraw money from accounts
acc1.withdraw(50000)
acc2.withdraw(50000)
#Show all accounts and balances
user1.show_accounts()