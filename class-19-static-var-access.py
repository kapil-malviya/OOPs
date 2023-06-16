"""

Accessing Static Variable : 

-> inside constructor : by using either self or classname
-> inside instance method : by using either self or classname
-> inside class method : by using either cls variable or classname
-> inside static method : by using classname
-> from outside of class : by using either object reference or classname

"""




class Test :
	a = 18
	def __init__(self) :
		print(self.a)
		print(Test.a)

	def m1(self) :
		print(self.a)
		print(Test.a)

	@classmethod        
	def m2(cls) :       
		print(cls.a)
		print(Test.a)       

	@staticmethod
	def m3() :
		print(Test.a)

t = Test()
t.m1()
Test.m2()     # t.m2()
Test.m3()     # t.m3()
print(t.a)
print(Test.a)


"""  output :

18
18
18
18
18
18
18
18
18         """




