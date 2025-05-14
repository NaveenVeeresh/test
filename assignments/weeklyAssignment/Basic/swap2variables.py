def swap2v(a, b):
    temp = a
    a = b
    b = temp
    return a, b


number1 = int(input("enter first No :"))
number2 = int(input("enter first No :"))

print(swap2v(number1, number2))
