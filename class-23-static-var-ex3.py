"""
various examples for static variable :


class Test :
	a = 8
	def __init__(self) :
		self.b = 9
	def m1(self) :
		self.a = 888
		self.b = 999

t1 = Test()
t2 = Test()
t1.m1()

print('t1 : ', t1.a, t1.b)     #  888  999
print('t2 : ', t2.a, t2.b)     #    8    9            



"""


class Test :
	a = 8                 # static var.
	def __init__(self) :
		self.b = 9        # instance var.

	@classmethod
	def m1(cls) :
		cls.a = 888       # static var. 
		cls.b = 999       # static var. 

t1 = Test()
t2 = Test()
t1.m1()

print('t1 : ', t1.a, t1.b)     #  888  9         if var. accessed by object reference then priority will be given to instance var. and after that static var.
print('t2 : ', t2.a, t2.b)     #  888  9            

print('Test : ', Test.a, Test.b)     #  888  999


"""
for modification of static variable, only use class name or cls (class method)

"""