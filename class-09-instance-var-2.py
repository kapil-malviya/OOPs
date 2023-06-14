"""

2- Inside Instance Method by using self variable :

	We can also declare instance variables inside instance method by using self variable. 
	If any instance variable declared inside instance method, that instance variable will 
	be added once we call that method,,


"""


class Test :
	def __init__(self) :
		self.a = 80
		self.b = 83

	def method1(self) :
		self.c = 88

t = Test()
print(t.__dict__)        #  =>> {'a': 80, 'b': 83} only two instance variables

t.method1()
print(t.__dict__)        #  =>>  {'a': 80, 'b': 83, 'c': 88}