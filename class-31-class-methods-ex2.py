
## Program to track the number of objects created for a class :


class Test :
	count = 0
	def __init__(self) :
		Test.count = Test.count + 1      # Test.count + = 1

	@classmethod                            
	def NOObjects(cls) :
		print('the number of objects created : ', cls.count)

t1 = Test()
t2 = Test()

Test.NOObjects()         #  the number of objects created : 2

t3 = Test()
t4 = Test()
t5 = Test()

t5.NOObjects()       # we can also access class method using object reference

#  =>>   the number of objects created : 5