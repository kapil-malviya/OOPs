"""
passing members of one class to another class : 

"""

class Employee :
	def __init__(self, eno, ename, esal) :
		self.eno = eno
		self.ename = ename
		self.esal = esal

	def display(self) :
		print('employee number : ', self.eno)
		print('employee name : ', self.ename)
		print('employee salary : ', self.esal)


class Test :
	def modify(emp) :            # static method
		emp.esal = emp.esal+8000
		emp.display()

#  We can access members of one class inside another class,

e = Employee(108, 'kapil', 888)
Test.modify(e)

