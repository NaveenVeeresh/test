# in python we raise exception in java we throw exception
# try:
#     print(x)
# # except:
# #     print('there is an error')
# except NameError:
#     print('name error')
#
from sys import exception


class myexception(Exception):
    pass


try:

    # print(5/0)
    #  if not type(5) is str:
    #      raise TypeError('only strings')
    # custom exception
    # raise Exception('my current exception')

    # if u want create a exception first create one then pass here

    raise myexception('my custom exception')

except ZeroDivisionError:
    print('ZeroDivisionError')
# except Exception as error:  # parent
#     print('error')
# else:  # only comes here when no error
#     print('no error')
# finally:
#     print('with or without error')
