'''

## Constructor Overriding :

-> if child class does not contain constructor then parent class constructor will be executed.,
-> from child class constuctor we can call parent class constructor by using super() method,.


class P :
	def __init__(self) :
		print('parent class constructor executed')

class C(P) : pass

c = C()         # parent class constructor executed

'''


class Person :
	def __init__(self, name, age) :
		self.name = name 
		self.age = age

class Employee(Person) :
	def __init__(self, name, age, eno, esal) :
		super().__init__(name, age)
		self.eno = eno
		self.esal = esal

	def display(self) :
		print('employee name : ', self.name)
		print('employee age : ', self.age)
		print('employee no. : ', self.eno)
		print('employee salary : ', self.esal)
		print()

e1 = Employee('kapil', 80, 888, 8000000)
e1.display()

e2 = Employee('anna', 79, 999, 9000000)
e2.display()




#  same name but multiple forms is the concept of polymorphism