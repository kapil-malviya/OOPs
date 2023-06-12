"""
#     Variables  &  Methods --> 

==> Within the Python class we can represent data by using variables. 
	There are 3 types of variables are allowed =>> 
		
	- static variables (Class Level Variables)
	- instance variables(non-static variables) (Object Level Variables)
	- local variables (Method Level Variables)
	- global variables 

==> Within the Python class, we can represent operations by using methods. 
	The following are various types of allowed methods =>>

	- Static Methods
	- Instance Methods (non-static methods)
	- Class Methods

"""


x = 88                           # ==> global variable (outside of the class)
class Employee :
	cmpname = 'RS & Sons'        # ==> static variable (inside of class but outside of constructor and method)
	def __init__(self, name, contact, city):
		self.name = name         #1 ==> instance variable(non-static variable)
		self.contact = contact   #2 ==> variables declared with self
		self.city = city         #3 ==> always declared inside of constructor
		y = 800                  # ==> local variable (inside of method or constructor but without self declaration)
	def method1(self):
		z = 888                  # ==> local variable (inside of method or constructor but without self declaration)