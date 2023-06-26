'''

Destructors :

-> Destructor is a special method and the name should be __del__()

-> Just before destroying an object Garbage Collector always calls 
	destructor to perform clean up activities (Resource deallocation 
	activities like close database connection etc).

-> Once destructor execution completed then Garbage Collector automatically 
	destroys that object.

-> The job of destructor is not to destroy object and it's just to perform clean up activities.
	and gc is responsible to destroy the object.,





import time

class Test :
	def __init__(self) :
		print('object initialisation...')

	def __del__(self) :
		print('fulfilling last wish and performing cleanup activities..')

t1 = Test()
t1 = None      # after this, the reference of t1 is no longer for Test(), here t1 is available for the future

time.sleep(5)      # for 5 seconds

print('end of application')


'''



import time

class Test :
	def __init__(self) :
		print('constructor execution...')

	def __del__(self) :
		print('destructor execution...')

t1 = Test()
del t1                #  here deleting t1 object completely

time.sleep(5)

print('end of application')