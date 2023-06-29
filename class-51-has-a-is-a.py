'''
Has-a Relation  vs  Is-a Relation  =>>


-> If we want to extend existing functionality with some more extra functionality then 
	we should go for IS-A Relationship.,

-> If we dont want to extend and just we have to use existing functionality then we 
	should go for HAS-A Relationship.,


'''


class Car :
	def __init__(self, name, model, color) :
		self.name = name
		self.model = model
		self.color = color

	def getinfo(self) :
		print("\tCar Name:{} \n\t Model:{} \n\t Color:{}".format(self.name, self.model, self.color))


class Person :
	def __init__(self, name, age) :
		self.name = name
		self.age = age

	def eatndrink(self) :
		print('Eat Biryani and Drink Beer')

class Employee(Person) :
	def __init__(self, name, age, eno, esal, car) :
		super().__init__(name, age)
		self.eno = eno
		self.esal = esal
		self.car = car

	def work(self) :
		print("Coding Python is very easy just like drinking Chilled Beer")

	def empinfo(self) :
		print("Employee Name : ", self.name)
		print("Employee Age : ", self.age)
		print("Employee Number : ", self.eno)
		print("Employee Salary : ", self.esal)
		print("Employee Car Info : ")
		self.car.getinfo()

c=Car("Innova", "2.5V", "Grey")
e=Employee('kapil', 28, 888, 8800000, c)
e.eatndrink()
e.work()
e.empinfo() 




'''

here, Employee class extends Person class functionality but just uses Car class functionality.             '''