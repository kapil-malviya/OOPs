'''

##  Inheritance  (IS-A Relationship) :

-> What ever variables, methods and constructors available in the parent class by default available to
	the child classes and we are not required to rewrite. Hence the main advantage of inheritance is
	Code Reusability and we can extend existing functionality with some more extra functionality.

Syntax :

	-> class childclass(parentclass):


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

class Y(X) :
	pass

o = Y()
print(o.a)       # 80      accessing static variable from class X

o.m1()           # accessing class X method, from child class
o.m2()
o.m3()
print(o.b)        # 888