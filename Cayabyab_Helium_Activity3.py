class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def get_account_number(self):
        return int(self.__account_number)

    @property
    def get_balance(self):
        return float(self.__balance)

    @get_account_number.setter
    def set_account_number(self, account_number):
        if account_number > 0 and type(account_number) == int:
            self.__account_number = account_number  
        else:
            print("Account number must not be a non-integer or a negative number.")


    @get_balance.setter
    def set_balance(self, balance): 
        print(f"Update balance to: {balance}")
        if balance >= 0 and type(balance) == float:
            self.__balance = balance
        else:
            print("Balance must not be a negative number.")

print("Account 1")
account1 = BankAccount(12345, 1000)
print(f"Account Number: {account1.get_account_number}")
print(f"Balance: {account1.get_balance}")
print()
account1.set_balance = -100
print(f"Account Number: {account1.get_account_number}")
print(f"Balance: {account1.get_balance}")