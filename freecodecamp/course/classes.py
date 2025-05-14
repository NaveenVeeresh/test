class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("moves along")

    def get_make_model(self):
        print(f"{self.make}, is {self.model}")


mycar = Vehicle('tesla', '3')
mycar.get_make_model()


# mycar.moves()
# class car(Vehicle):
#     def moves(self):
#         print(f"drives in a highway")
#

class cart(Vehicle):
    pass  # means it inherits all from parent


# secar = car('abc', '434')
# secar.get_make_model()

acrt = cart('gocart', '3')
acrt.get_make_model()


class car(Vehicle):

    # if u want to add new attribute copy init and call the parent add the new one
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.make = make
        self.model = model
        self.year = year

    def get_make_model(self):
        print(f"{self.make}, is {self.model},{self.year}")

    def moves(self):
        print(f"drives in a highway")


acar = car('esteem', 'vxi', '2005')
acar.get_make_model()


#polymorphism

#have same methods may have functionality different
for v in (acar,acrt,mycar):
    v.get_make_model()
    v.moves()
