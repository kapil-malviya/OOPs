## Program to track the number of objects created for a class : directly with static method in generalised way ;


class Test :
	count = 0
	def __init__(self) :
		Test.count = Test.count + 1      # Test.count + = 1
                         
	def NOObjects() :
		print('the number of objects created : ', Test.count)

t1 = Test()
t2 = Test()

Test.NOObjects()

#  =>>  the number of objects created :  2