l=[1,2,3,4]
print(1 in l)  #return True  boolean value

#in dict it considers key
d={'a':1,'b':2}
print('a' in d)  #return True  boolean value
print(1 in d)  #return False  boolean value

#for assginment
additional_data.pop('support')

del addtional_data['support']

#which is better?
#pop() is better because it returns the value of the key that is removed
#del is better because it does not return anything
#del deletes memory of that key
from typing import Dict
import  requests
response=requests.get('http://httpbin.org/get')



import  json
#json.dump() write a variable to a file pointer
#json.dumps() write a variable to a string
#json.load() read a variable from a file pointer
#json.loads() read a variable from a string

#json.dumps() converts a Python object into a JSON string
#json.loads() converts a JSON string into a Python object

json.dumps({'a':1,'b':2})=json.loads('{"a":1,"b":2}')


customer_id->
grep customer_id

#implimenting using generator  and yield











