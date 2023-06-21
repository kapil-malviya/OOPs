'''

###  Methods :

==> Within the Python class, we can represent operations by using methods. 
	The following are various types of allowed methods =>>

	- Instance Methods (non-static methods) (object related method)
	- Static Methods
	- Class Methods


##  Instance Method =>

	-> Inside method implementation if we are using instance variables then such 
		type of methods are called instance methods.

	-> Inside instance method declaration, we have to pass self variable.

		def m1(self) :

	-> By using self variable inside method we can able to access instance variables.

		def m1(self) :
			print('student name : ', self.name)

	-> Within the class we can call instance method by using self variable and 
		from outside of the class we can call by using object reference.


'''



class Student :
	def __init__(self, name, marks) :
		self.name = name 
		self.marks = marks

	def display(self) :
		print('hii ', self.name)
		print('you got ', self.marks,'marks')

	def grade(self) :
		if self.marks >= 60 :
			print('you got First grade')
		elif self.marks >= 50 :
			print('you got Second grade')
		elif self.marks >= 35 :
			print('you got Third grade')
		else :
			print('you are failed')

n = int(input('Enter number of students : '))
for i in range(n) :
	name = input('Enter name : ')
	marks = int(input('Enter marks : '))
	s = Student(name,marks)
	s.display()
	s.grade()
	print()