# demo example : super() method ;

class Person :
	def __init__(self, name, age) :
		self.name = name
		self.age = age

	def eatanddrink(self) :
		print('biryani with JD')

class SE(Person) :
	def __init__(self, name, age, eno, esal) :
		super().__init__(name, age)
		self.eno = eno
		self.esal = esal

	def work(self) :
		print('python coding is something like having chilled beer')

s=SE('kapil', 88, 8888, 8800000) # invalid line untill calling name & age from parent class via super()

print(s.name, s.age, s.eno, s.esal)     #  kapil 88 8888 8800000
s.eatanddrink()
s.work()