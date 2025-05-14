even = []
def even_num(n):
    for i in n:
        if i % 2 == 0:
            even.append(i)
    return even


numbers = [1, 2, 3, 4, 6, 8]

num=input()
print(even_num(numbers))
