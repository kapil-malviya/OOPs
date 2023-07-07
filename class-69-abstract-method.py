'''
#   Abstraction :
	
	- Abstract method
	- Abstract class
	- Interface


## Abstract Method :

-> sometimes we don't know about the implementation, still we can declare
	a method, such type of methods are called abstract method. 
	i.e. abstract method has only declaration but not implementation

-> in python we can declare abstract method by using @abstractmethod decorator :
	
	@abstractmethod
	def m1(self) : pass

-> abstractmethod decorator present in abc module, hence compulsory we should
	import abc module, otherwise we'll get error.,

	abc -> abstract base class module


# child classes are responsible to provide implementation for parent class abstract methods.



from abc import *
class Vehicle :
	@abstractmethod
	def getNoOfWheels(self) :
		pass

'''

from abc import *
class Fruit :
	@abstractmethod
	def taste(self) :
		pass



