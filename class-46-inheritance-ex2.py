'''
# Inheritance (Is-a Relationship) : priority of objects in child class

-> What ever methods present in Parent class are automatically available to the 
	child class and hence on the child class reference we can call both parent 
	class methods and child class methods.

'''


class X :
	a = 80
	def m1(self) :
		print('parent class instance method')

	@classmethod
	def m2(cls) :
		print('parent class class method')

	@staticmethod
	def m3() :
		print('parent class static method')

	def __init__(self) :
		self.b = 888
		print('parent constructor')

	def __del__(self) :
		print('parent destructor')

class Y(X) :
	a = 90
	def __init__(self) :
		print('child class constructor...')

	def __del__(self) :
		print('child class destructor..')

y = Y()

print(y.a) 



'''  =>>  

parent constructor
90                    => priority to the child class
parent destructor                                    '''


## after adding child class constructor and child class destructor : 

'''  =>> 

child class constructor...
90
child class destructor..                   '''


'''

-> in all cases (constructor, variables, methods) priority will always 
	be given to the child class(constructor, methods, destructor, 
	variables) if child class doens't have any of this then the 
	reference class (constructor, variables, methods, destructor) will 
	be given priority


'''