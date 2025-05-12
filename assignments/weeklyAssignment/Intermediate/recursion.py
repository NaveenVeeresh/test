def recursion(n):
    if n == 1:
        return 1
    return n * recursion(n - 1)


recurs =int(input("enter the number"))
print(recursion(recurs))