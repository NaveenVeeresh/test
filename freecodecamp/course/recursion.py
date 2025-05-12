def add_one(num):
    if num >= 9:
        return num + 1

    total = num + 1
    print(total)
    return add_one(total)


# add_one(0)

# using for loop
def add_two(num):
    for i in range(num, 9):
        total = i + 1
        print(total)
        if total >= 9:
            return total
    return total


# add_two(0)
# print(add_one(0))


value ='y'
count=0

while value:
    count+=1
    print(count)
    if count==5:
        break
    else:
        value=0
        continue

