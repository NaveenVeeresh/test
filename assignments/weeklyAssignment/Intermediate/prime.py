def is_prime(n,i=2):
    if n<=1:
        return False
    if i*i >n:
        return True
    if n%i==0:
        return False

    return is_prime(n,i+1)

number=int(input("enter ur number"))
if is_prime(number):
    print(f"{number} is a prime")
else:
    print(f"{number} is not prime")