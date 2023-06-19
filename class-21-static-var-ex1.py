"""
various examples for static variable :

"""


class Test :
	a = 88
	def m1(self) :
		self.a = 888      # not permormimg change to static var. but creating instance var.
#		Test.a = 999

t1 = Test()
t1.m1()
print(Test.a)   #  88   < accessing static var.
print(t1.a)     # 888   < accessing instance var. (bcoz we access instance var. by using object reference only)

