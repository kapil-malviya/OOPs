'''

## Class Methods :

-> Inside method implementation if we are using only class variables 
	(static variables), then such type of methods we should declare as class method.

-> We can declare class method explicitly by using @classmethod decorator.

-> For class method we should provide cls variable at the time of declaration

-> We can call classmethod by using classname or object reference variable. 
	(recommended to use classname while calling or accessing)

Syntax : 

	@classmethod
	def m1(cls) :
		cls.x
		classname.y


'''


class Animal :
	legs = 4             # class level var. (static var.)
	@classmethod
	def walk(cls, name) :
		print('{} walks with {} legs'.format(name, cls.legs))       # using static var. (legs) here

Animal.walk('Dog')
Animal.walk('Cat')




"""
instance method means : using instance variable &
class method means : using class variable

"""