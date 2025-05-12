# loops
# while and for

value = 1
# while value<10:
#     print(value)
#     if value==5:
#         break
#     value+=1

# while value < 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)


#for loop

names={'navven','dkos','sdmiosdj','skjdjs'}
# for i in names:
#     print(i)
#
# #
# for i in 'skjksdkskd':
#     print(i)
print('==================================')

# for i in names:
#     # print(i)
#     if i == 'sdmiosdj':
#         break
#     print(i) #print previous element before it equals

# for i in names:
#     if i == 'sdmiosdj':
#         continue  # except this print everything
#     print(i)

#in range

# for x in range(4):
#     print(x)
#
# for x in range(2,8):
#     print(x)

#increment
#
# for x in range(1,100,5):
#     print(x)


# for x in range(1,100,5):
#     print(x)
# else:
#     print("over!!!!")
#
#



# names1={'naveen','ramesh','siren','similar'}
# actions ={'codes','eats','sleep'}
# for name in names1:
#     for action in actions:
#         print(name+'  '+action)
#
#
#



 #function
def name(n=0,n1=0):
     print(n+n1)


name()
name(2,3)


#more parameters
def multiple_items(*args): #u can use args or any name
    print(args)
    print(type(args))


multiple_items(1,2,3)

def multiple_item1s(**kwargs): #we use more this
    print(kwargs)
    print(type(kwargs))


multiple_item1s(first=1,second=2)

