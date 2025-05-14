class balanceexception(Exception):
    pass


class bankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\n Account '{self.name}' Bank Account is  created with  \n  Balance =${self.balance:.2f}  ")

    # self.balance:.2f means round upto 2 decimal points
    def getbalance(self):
        print(f"\n Account '{self.name}' has a   \n  Balance =${self.balance:.2f}  ")

    def deposit(self, amount):
        self.balance += amount
        print("deposit completed")
        self.getbalance()

    def viabletransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise balanceexception(f"insufficient balance")

    def withdraw(self, amount):
        try:
            self.viabletransaction(amount)
            self.balance -= amount
            print("withdraw successfull")
            self.getbalance()
        except balanceexception as error:
            print(f"\n withdraw interrupted:{error}")

    def transfer(self, amount, account):
        try:
            print("\n transfer starts")
            self.viabletransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            self.getbalance()
            print("success")

        except balanceexception as error:
            print(f"interupted : {error}")
