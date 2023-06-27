'''

Composition  and  Inheritance :

-: how we can use members of one class inside another class : (two ways)

	-> by using Composition (has-a relationship)
	-> by using Inheritance (is-a relationship)


## by using Composition (Has-a Relationship) =>>

	-> by using Class Name or by creating object we can access members of one class inside another class
		is nothing but composition (Has-A Relationship). 

	-> code reusability

'''


class Car :
	def __init__(self, name, model, color) :
		self.name = name
		self.model = model
		self.color = color

	def getinfo(self) :
		print('Car Name : {}, Model : {}, Color : {}'.format(self.name, self.model, self.color))

class Employee :
	def __init__(self, ename, eno, car) :
		self.ename = ename
		self.eno = eno
		self.car = car

	def empinfo(self) :
		print('Employee Name : ', self.ename)
		print('Employee number : ', self.eno)
		print('Employee Car info : ')
		self.car.getinfo() 

c = Car('Defender', '4L D', 'Black')
e = Employee('Kapil', 88, c)
e.empinfo()




'''

here, Employee class Has-A Car reference and hence Employee class can access all
members of Car class.     '''