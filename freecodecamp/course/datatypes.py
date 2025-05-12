
# string data type
# literal string
name = "naveen"

print(type(name))
print(type(name) == str)
print(isinstance(name, str))

# concatenation
firstname = "Naveen"
lastname = "Veeresh"
fullname = firstname + "" + lastname
fullname+= "!"
# print(fullname)

#Casting number to string

num =str(2025-1999)
# print(fullname+" current age : "+num)

#multiple lines
multi ='''
hey how are u?
i was just checking in!!         
'''
# print(multi)

#escaping special characters
sentence='I\'m back!\t hey\n \located?'
# print(sentence)

#string methods
# print(fullname)
# print(id(fullname))
# print(fullname.lower())
# print(fullname.upper())
# print(id(fullname))
# print(multi.title())
# print(sentence.replace("back","late"))
# print(len(sentence))

#strip removes white space
sentences="hi hello           im naveen       "
sentences+= "                       "
print(sentences)

print(len(sentences))
print(len(sentences.strip())) #removes white space
print(len(sentences.lstrip()))#removes left white space and rstrip to right

#center
title = "menu".upper()
print(title.center(20,"="))
print("Coffee".ljust(16,"=")+"$1".rjust(4)) #o/p=>  Coffee==========  $1

#index
naam ="hello everybody!"
print(naam[0]) #first
print((naam[-1])) #last
print(naam[1:-1])#ignoring last
print(naam[1:])
#boolean
myval=True
x=bool(myval)
print(isinstance(myval,bool))
print(type(x))

#integer
y=23
print(type(y))
print(type(y) == int)

#float
gpa=8.907
print(round(gpa))
#complex value
comp_value=2+23j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)
print(comp_value.__abs__()) #absolute value

#abs
z=23.666293
print(abs(z))
print(round(z))
print(abs(z*-1))
import math
# za=math.ceil(z)
# print(za)
print(math.pi)
print(math.factorial(2))
print(math.floor(23.97778))







