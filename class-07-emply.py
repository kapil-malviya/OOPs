

class Employee :
	def __init__(self, eno, ename, esal, ecity) :
		self.eno = eno
		self.ename = ename
		self.esal = esal
		self.ecity = ecity

	def display(self) :
		print('employee no : ', self.eno)
		print('employee name : ', self.ename)
		print('employee salary : ', self.esal)
		print('employee city : ', self.ecity)

e1 = Employee(101,'harsh',50000,'bholaram\n')
e1.display()

e2 = Employee(102,'ammit',51000,'mr10')
e2.display()