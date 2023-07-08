'''

#  Public, Protected and Private Attributes : 

-> by default every attribute is public, we can access from anywhere either within the 
	class or from outside of the class.
	
	eg : 
	name = 'kapil'

-> protected attributes can be accessed within the class anywhere but from outside of 
	of the class only in child classes. we can specify an attribute as protected
	by prefixing with _ symbol

	syntax : 

	_variablename = value

	eg : 
	_name = 'kapil'

	- but it is just convention and in reality, protected attribute doesn't exist 

-> private attribute can be accessed only within the class. i.e. from outside of the class 
	we can't access. We can declare a variable as private explicitly by prefixing with
	(__) 2 underscore symbols

	syntax : 
	__variablename = 'kapil'

	eg : 
	__name = 'kapil'




class Test :
	x = 8
	_y = 80
	__z = 888
	def m1(self) :
		print(Test.x)
		print(Test._y)
		print(Test.__z)

t = Test()
t.m1()

'''

class Test :
	def __init__(self) :
		self.__x = 88

	def m2(self) :
		print(self.__x)      # 88

t = Test()
t.m2()

# print(t.__x)   =  AttributeError: 'Test' object has no attribute '__x'

# outside of the class we are not allowed to access the private variable


'''

-> accessing private variable from outside of the class : 

	-> we can not access private variables directly from outside of the class
	-> but we can access indirectly as follows : 

	objectreference._classname__variablename

'''

print(t._Test__x)         # 88