from email.contentmanager import raw_data_manager

# In Python, tuples, lists, and dictionaries are three different types of data structures with distinct properties:
#
# 1. Tuple (tuple)
# Immutable: Once created, elements cannot be changed, added, or removed.
# Syntax: Defined with parentheses ().
# my_tuple = (1, 2, 3)
# Use Case: Best for fixed collections
# .
# 2. List (list)
# Mutable: Elements can be modified after creation.
# Syntax: Defined with square brackets [].
# my_list = [1, 2, 3]
# Use Case: Best for dynamic collections where changes are needed
# .
# 3. Dictionary (dict)
# Key-Value Pairs: Stores data as {key: value} pairs
# .
# Mutable: Values can be modified, and keys can be added/removed.
# Syntax: Defined with curly braces {}.
# my_dict = {"a": 1, "b": 2}


#List and its properties
users=["naveen","ramesh","suresh"]
data=["ramesh",23,True]
print("naveen" in users)
print(users[:2]) # does not include 2th element
print(users.index("suresh"))
print(users[0:1])# includes 0 as start ['naveen']
print(users[:2])# includes ['naveen', 'ramesh']
print(users[-3:-1])# includes ['naveen', 'ramesh']
print(users[0:2])# includes 0 as start ['naveen'
print(users[-3:])# includes ['naveen', 'ramesh', 'suresh']


#append
users.append("mona")
print(users)
users.extend(["i","we","us"])
users+=['jason']  #users+= 'jason'  // it will take each character as a list item
print(users)
#insert
users.insert(1,"naddy")
print(len(users))
users[2:2]=['name','sureshaa'] #insert 2 values at second position
print(users)
print(len(users))

users.remove("name")
print(users)
print(users.pop())
print(users)

#to delete
del users[0]
print(users)
del  data #throws errors
# print(len(users))
users.sort() #if u have lowercase then it comes at last
print(users)
#to add irrespective
users.append("apple")
users.sort(key=str.lower)
print(users)

#numbers
num= [1,34,7,9,56]
num.reverse()
print(num)
num.sort()
print(num)
#to copy
mycopy=num.copy()
nums=list(num)
cid=num[:]
print(cid)

#tuples
#not change
random=(2,3,4,5)
print(random)
liftoff=list(random)
liftoff.append(23)
print(tuple(liftoff))

#u can name them
# (one,two,*last) =random # *last makes a tuple of all elements
(one,*two,last) =random # *last makes a tuple of all elements

print(one)
print(two)
print(last)

#u can use count to count  the item in tuple
print(random.count(2))






