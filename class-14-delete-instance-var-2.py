# another excample of deleting insance variable : 


class Test :

	def __init__(self) :
		self.a=10
		self.b=20
		self.c=30
		self.d=40

	def m1(self) :
		del self.d

t = Test()
print(t.__dict__)     

# =>>   {'a': 10, 'b': 20, 'c': 30, 'd': 40}

t.m1()
print(t.__dict__)   

# =>>   {'a': 10, 'b': 20, 'c': 30}

del t.c
print(t.__dict__)

# =>>   {'a': 10, 'b': 20}