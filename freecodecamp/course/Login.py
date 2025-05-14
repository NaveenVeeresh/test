# list of objects
from typing import Optional, List


class Product:
    def __init__(self, product_name, price, brand):
        self.product_name = product_name
        self.price = price
        self.brand = brand


products = [
    Product("Air conditioner", 1500, "Carrier"),
    Product("Latop", 70500, "Dell"),
    Product("iPad", 80500, "Apple")
]
"""
We are calling the class to create each object; and all those objects will be wrapped in a list
"""
print(products)
for product in products:
    print(vars(product))


def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(f"Item: {item_name}, Price: {item_price}")


price = {'nrushi': 2000.23, 'nashit': 3000.23, 'nashit2': 4000.23}
process_items(price)


# union or optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


hi = say_hi("Nashit")


# Optional is used to indicate that a value can be of a certain type or None
# oneperson:Person is instance of Person class
class Person():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


def get_person(oneperson: Person):
    print(f"Name: {oneperson.name}, Age: {oneperson.age}")
    return oneperson


person = Person("Nashit", 23)
get_person(person)

from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    signup_date: datetime | None = None
    is_active: bool = True
    friends: List[int] = []


external_data = [
    {"id": 123,
     "name": "John Doe",
     "signup_date": "2023-10-01T12:00:00",
     "is_active": True,
     "friends": [1, 2, 3],
     },
    {"id": 456,
     "name": "Jane Doe",
     "signup_date": "2023-10-02T12:00:00",
     "is_active": False,
     "friends": [4, 5, 6],
     },
]

users = [User(**data) for data in external_data]
print(users)
