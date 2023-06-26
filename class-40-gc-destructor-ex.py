'''

-> If the object does not contain any reference variable then only it is 
	eligible fo GC. ie if the reference count is zero then only object 
	is eligible for GC


'''


import time

class Test :
	def __init__(self) :
		print('constructor execution...')

	def __del__(self) :
		print('destructor execution...')

t1 = Test()
t2 = t1
t3 = t2

del t1

time.sleep(5)
print('object not yet destroyed after deleting t1')

del t2

time.sleep(5)
print('object not yet destroyed after deleting t2')
print('trying to delete t3 also')

del t3



# destructor will execute only when object will be destroyed...


