'''

Inner classes/Nested class :

-> Sometimes we can declare a class inside another class, such type of classes are 
	called inner classes.

-> Without existing one type of object if there is no chance of existing another 
	type of object, then we should go for inner classes.

* Example : Without existing Car object there is no chance of existing Engine object. 
			Hence Engine class should be part of Car class.

	class Car :
		.....
		class Engine :
			......


* Example : Without existing university object there is no chance of existing 
			Department object.

	class University/(Human) :
		.....
		class Department/(Head) :
			......


'''


class Outer :
	def m1(self) :
		print('Outer class method...')

	class Inner :
		def m2(self) :
			print('Inner class method...')

'''
o = Outer()
o.m1()
o = o.Inner()
o.m2()             

=> output :
	
	Outer class method...
	Inner class method...                '''


i = Outer().Inner()
i.m2()

# output :  Inner class method...