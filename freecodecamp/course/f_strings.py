import modules


print(modules.capital+" :")

person='Dave'
coins=3

print(f"{person} has these {coins} in thier pocket")
print(f"{person.upper()} has these {coins} in thier pocket")

num=10
print(f"{2.25} times of num {2.25*num:.2f}") #num:.2f means 2 fixed decimal values

#in loop
for num in range(1,11):
    print(f"2.25 times of {num} is {2.25*num:.3f}")

for num in range(1,11):
    print(f"2.25 times of {num} is {num/2.25:.3%}")