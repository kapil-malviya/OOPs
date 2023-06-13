


class Student :
	def __init__(self, m='', n=8) :
		self.name = m
		self.marks = n

	def display(self) :
		print('hii ', self.name)
		print('you got ',self.marks,'marks')

s = Student()
s.display()

x = Student('kapil', 88)
x.display()