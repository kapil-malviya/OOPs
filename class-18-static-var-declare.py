"""

Various places to declare static variable : 

->  In general we can declare within the class directly but from out side of any method
->  Inside constructor by using class name
->  Inside instance method by using class name
->  Inside classmethod by using either class name or cls variable
->  Inside static method by using class name
->  From outside of the class by using classname

"""


class Test :
	a = 18
	def __init__(self) :
		self.b = 28         # instance variable
		Test.c = 38         # static variable, using class name

	def m1(self) :
		self.d = 48
		Test.e = 58

	@classmethod            # by using this decorator it'll consider the following method as class method
	def m2(cls) :           # class method
		cls.f = 68          # static variable
		Test.g = 78         # static variable

	@staticmethod
	def m3() :
		Test.h = 88


# to know all static variable  =>>  Test.__dict__

print(Test.__dict__)   # =>> only a (static var.) will be shown

t = Test()
print(Test.__dict__)    # here both a & c var. will be shown only after calling class

t.m1()
print(Test.__dict__)    # a, c & e var. will be shown only after calling m1 method

Test.m2()   # t.m2()
print(Test.__dict__)    # a, c, e, f & g

Test.m3()   # t.m3()
print(Test.__dict__)    # a, c, e, f, g & h var. will be shown after calling m3 method only


Test.i = 98         # declaring static var. outside f the class
print(Test.__dict__)    # a, c, e, f, g, h & i   variable will be shown


# explicitly accessing static variables =>

print(t.a, t.c, t.e, t.f, t.g, t.h, t.i)      # =>>  18 38 58 68 78 88 98