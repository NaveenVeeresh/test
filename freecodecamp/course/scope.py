# global
name = "Naveen"
from rpsi import rock_paper_scsissors

# def greeting():
#     print(name)
#
# greeting()
#

# def greeting(name):
#     color ='blue'
#     print(color)
#     print(name)



# def another():
#     greeting(name) #naveen
#
# another()

#nested
# def another():
#     color = "blue"
#     def greeting(name):
#         print(color)
#         print(name)
#     greeting("suresh")
#
# another()

count =1
def another():
    color = "blue"
    global count #use like this to access global variable
    count+=23
    print(count)
    def greeting(name):
        nonlocal color #to assign local variable not parent one
        color ='red'
        print(color)
        print(name)
    greeting("suresh")

another()

rock_paper_scsissors()