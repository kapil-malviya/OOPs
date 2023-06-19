"""

Local variable :

	-> Sometimes to meet temporary requirements of programmer, we can declare variables 
		inside a method directly, such type of variables are called local variable or 
		temporary variables.

	-> Local variables will be created at the time of method execution and destroyed 
		once method completes.

	-> Local variables of a method cannot be accessed from outside of method.


"""


class Test :
	def m1() :
		i = 0                  # local variable to hold the current value
		while i<8 :
			print('money')
			i+=1

Test.m1()


"""   output => 

money
money
money
money
money
money
money
money         """