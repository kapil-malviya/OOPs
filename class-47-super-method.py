'''  for accessing parent class objects from child class : 

super() -> super() is a built-in method which is useful to call the super class 
			constructors, variables and methods from the child class..,

super.x
super.m1()


-> In case of variables, super method is allowed to access only class level 
	variable and not instance variables.,

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
	a = 8888
	def __init__(self) :
#		super().__init__()
		print('child class constructor...')
		super().__init__()                      # we cam take super class method anywhere in the constructor 
		super().m1()
		super().m2()
		super().m3()
		print(super().a)
		print(Y.a)

y = Y()



''' =>> without adding super method =>> 


child class constructor....
parent class destructor                         '''


# after adding super() method and calling constructor of parent class : 

"""

parent constructor
child class constructor...
parent destructor                             """


## after calling various methods & variable of the parent class : 

''' =>> 

child class constructor...
parent constructor
parent class instance method
parent class class method
parent class static method
80
8888
parent destructor                                    '''