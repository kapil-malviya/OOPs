'''
# interface  vs  abstract class  vs  concrete class

-> if we don't know anything about implementation just we have the requirement
	specification then we should go for interface

-> if we are talking about implementation but not completely (partially implemented class)
	then we should go for abstract class

-> if we are talking about implementation completely and ready to provide service then we
	should go for the concrete class


'''


from abc import *

class CollegeAutomation(ABC) :
	@abstractmethod
	def m1(self) : pass

	@abstractmethod
	def m2(self) : pass

	@abstractmethod
	def m3(self) : pass

class AbsCls(CollegeAutomation) :
	def m1(self) :
		print('m1 method implementation')

	def m2(self) :
		print('m2 method implementation')

class ConcreteCls(AbsCls) :            # also include m1 and m2 method
	def m3(self) :
		print('m3 method implementation')


c = ConcreteCls()
c.m1()
c.m2()
c.m3()