"""
class and objects
inheritance
polymorphism
abstraction
encapsulation
"""


class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        print(f"Employee: {self.name},ID:{self.emp_id} ")


#
# emp_name = input("enter ur name")
# emp_id = input(int())
# empl1 = Employee(emp_name, emp_id)
# # empl1.get_info()


##inheritance
class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def get_info(self):
        super().get_info()
        print(f"Team Size : {self.team_size}")


manager = Manager("Naveen", 203, 1)
# manager.get_info()


##polymorphism
class developer(Employee):
    def get_info(self):
        super().get_info()


people = [Employee("naveen", 124), developer("suresh", 23)]

# for i in people:
#     i.get_info()


##encapsulation
# restricting
#balance is a private here

class BankAccout():
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance  # __abc is private _abc protected


account = BankAccout(7000)
account.deposit(123)
print(account.get_balance())


#create a venv
#adds all installs in virtual rather than system
#routes => url and routes are defined
#from typing import list,Optional
#from tasks
#__init__.py have to be created for easy to take in package
#celery(Workers)
#reddis
#routes
#uvicorn =>takes route gives u url

