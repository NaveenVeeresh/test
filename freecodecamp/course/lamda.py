from freecodecamp.course.recursion import add_two


def squared(num): return num * num


# both are same use lamda as a anonymous function

squared1 = lambda num: num * num
addtwo = lambda num: num + 2
addone = lambda a, b: a + b
#
# print(squared1(2))
# print(addtwo(20))
# print(addone(4,5))

#function builder

def funcbuilder(x):
    return lambda num: num+x

onedata=funcbuilder(10) # x=10
secondata=funcbuilder(20)# x=20

print(onedata(7)) #num=7
print(secondata(7))#num=7


numbers=[1,3,5,7,9,10,12,14]
sqaured_num=map(lambda num:num*num,numbers)
print(list(sqaured_num))

even_func=filter(lambda num:num%2 !=0,numbers)
print(list(even_func))


from functools import reduce
#basically adds the values

total=reduce(lambda acc,curr:acc+curr,numbers)
print(total)
print(sum(numbers))#built in functions

#add more
total=reduce(lambda acc,curr:acc+curr,numbers,10)
print(total)
print(sum(numbers,10))

#character value u should add 0 as initial
#adds all characters in the list

names=['Naveen Veeresh','suresh','sachin','dhshdd']

name=reduce(lambda acc,curr:acc+len(curr),names,0)
print(name)

