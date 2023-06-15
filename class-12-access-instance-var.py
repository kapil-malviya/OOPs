"""

How to access Instance variables :

	We can access instance variables with in the class by using self variable 
	and outside of the class by using object reference,

"""


class Test :
	def __init__(self) :
		self.a = 80
		self.b = 88

	def display(self) :
		print(self.a)
		print(self.b)

t = Test()
t.display()
print(t.a, t.b)