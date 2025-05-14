# count=0
def countvowels(n):
    vowels = "aeiouAEIOU"
    count = 0

    for char in n:
        if char in vowels:
            count += 1
    return count


user = input("enter the word ")
print(countvowels(user))

countvowels('abcdef')
