##  Abstract Class  :
'''

-> sometimes implementation of a class is not complete, such type of partially implementation 
	classes are called abstract classes. 
-> every abstract class in python should be derived from ABC class which is present in 
	abc module




from abc import *

class Vehicle(ABC) :
#	@abstractmethod
	def getNoOfWheels(self) :
		print('hello')

v = Vehicle()
v.getNoOfWheels()

'''

# TypeError: Can't instantiate abstract class Vehicle with abstract method getNoOfWheels



'''
-> if class extending ABC class and contains atleast one abstract method,
	then object creation is not possible.

-> if class extending ABC class and doesn't contain any abstract method, then object 
	creation is possible

-> abstract class can contain multiple methods, even some concrete methods

-> abstract class can contain both abstract methods and normal methods

-> child classes are responsible to provide proper implementation of parent class abstract methods

'''


from abc import *

class Vehicle(ABC) :
	@abstractmethod
	def getNoOfWheels(self) :
		pass

class Bus(Vehicle) : 
	def getNoOfWheels(self) :
		return 7

class Auto(Vehicle) : 
	def getNoOfWheels(self) :
		return 3


b = Bus()
print(b.getNoOfWheels())     # 7


a = Auto()
print(a.getNoOfWheels())     # 3