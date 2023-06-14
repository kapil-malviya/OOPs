"""

3- Outside of the class by using object reference variable :
	
	We can also add instance variables outside of a class to a particular object.
	By using one object reference if we perform any change to the instance 
		variables, the changes won't affect the remaining ojects,,




class Test :
	def __init__(self) : 
		self.x = 80 

t1 = Test()
t2 = Test()
print(t1.x, t2.x)      # =>> 80  80
print()

t1.x = 88
print(t1.x, t2.x)      # =>> 88  80

"""


class Test :
	def __init__(self) : 
		self.a = 80
		self.b = 83

	def m1(self) :
		self.c = 88

t = Test()
print(t.__dict__)    # =>>  {'a': 80, 'b': 83}

t.m1()
print(t.__dict__)    # =>>  {'a': 80, 'b': 83, 'c': 88}

t.d = 888            # adding instance variable outside of the class by using reference variable..
print(t.__dict__)    # =>>  {'a': 80, 'b': 83, 'c': 88, 'd': 888}
