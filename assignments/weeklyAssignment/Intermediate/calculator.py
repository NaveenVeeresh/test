from random import choice


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "Error : cannot divide by zero"
    return a/b

num1=float(input("enter the first number"))
num2=float(input("enter the second number"))


print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice =input("Enter ur choice 1/2/3/4 ")

if choice=='1':
    print("Result:",add(num1,num2))
elif choice == '2':
    print("Result:", sub(num1, num2))
elif choice == '3':
    print("Result:", mul(num1, num2))
elif choice == '4':
    print("Result:", div(num1, num2))
else:
    print("Invalid choice.")





