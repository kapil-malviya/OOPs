'''

Setter and Getter Methods :

-> We can set and get the values of instance variables by using setter and getter methods.

## Setter Method :

	-> setter method can be used to set values to the instance variables, setter method 
		is also known as mutator method.
	
	Syntax :

		def setVariable(self,variable):
			self.variable=variable
	
	Example :

		def setName(self,name) :
			self.name=name

## Getter Method :

-> Getter method can be used to get values of the instance variables. Getter method 
	is also known as accessor method.

	Syntax :

		def getVariable(self) :
			return self.variable

	Example :
	
		def getName(self) :
			return self.name                                                                           '''



class Student :

	def setName(self, name) :
		# can also add validation logic
		self.name = name

	def getName(self) :
		return self.name 

	def setMarks(self, marks) :
		self.marks = marks

	def getMarks(self) :
		return self.marks

n = int(input('Enter no. of students : '))
for i in range(n) :
	s = Student()
	name = input('Enter name of student : ')
	s.setName(name)
	marks = int(input('Enter marks of student :'))
	s.setMarks(marks)

	print('hi ', s.getName())
	print('you got ', s.getMarks(),'marks')
	print()