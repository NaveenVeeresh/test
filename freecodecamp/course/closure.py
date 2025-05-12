#Closure is a function having access to the scope of its parent
#function after the parent function returned



# def parent_function(person):
#     coins=3
#     def game_coin():
#         nonlocal coins #using because changing global values it takes coins as global not create one
#         coins-=1
#         if coins>1:
#             print(f"\n {person} with coins left {coins}")
#         elif coins==1:
#             print(f"\n {person} with coin left {coins}")
#         else:
#             print(f"no coins left")
#
#     return game_coin #you're not returning method function returning method itself
#                         #this is called closure when child is returned or closed
#                         #have access to global var

def parent_function(person,coins): #u can pass as param
    #coins=3
    def game_coin():
        nonlocal coins #using because changing global values
        coins-=1
        if coins>1:
            print(f"\n {person} with coins left {coins}")
        elif coins==1:
            print(f"\n {person} with coin left {coins}")
        else:
            print(f"no coins left")

    return game_coin #you're not returning method function returning method itself
                        #this is called closure when child is returned or closed
                        #have access to global var


tommy=parent_function("Tommy",3)
jenny=parent_function("jenny",4)

tommy()
tommy()

jenny()
tommy()




