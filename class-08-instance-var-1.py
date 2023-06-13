"""

Variables :

	==> Within the Python class we can represent data by using variables. 
		There are 3 types of variables are allowed =>> 
	
	- instance variables(non-static variables) (Object Level Variables)
	- static variables (Class Level Variables)
	- local variables (Method Level Variables)
	- global variables 



###  Instance Variable (non-static variable) =>> 

	If the value of a variable is varied from object to object, then such type of variables 
	are called instance variables,
	For every object a separate copy of instance variables will be created,


	-> Where we can declare Instance variables :
		1- Inside Constructor by using self variable
		2- Inside Instance Method by using self variable
		3- Outside of the class by using object reference variable (where constructor is called)





1- Inside Constructor by using self variable :
	We can declare instance variables inside a constructor by using self keyword,
	Once we creates object, automatically these variables will be added to the object.

"""


class Student :
	def __init__(self, name, rollno, marks) :
		self.name = name 
		self.rollno = rollno
		self.marks = marks

	def display(self) :
		print('students name : ', self.name)
		print('students rollno : ', self.rollno)
		print('students marks : ', self.marks)
		print()

s1 = Student('anna', 101, 95)
s2 = Student('paritosh',102,93)
s3 = Student('lokesh',103,96)

# s1.display()
# s2.display()
# s3.display()

# print(s1.name, s1.rollno, s1.marks)
# print(s1.name, s2.name, s3.name)

# for knowing how many instance variable has been created, for that : 

print(s1.__dict__)       # =>>   {'name': 'anna', 'rollno': 101, 'marks': 95}
print(s3.__dict__)       # =>>   {'name': 'lokesh', 'rollno': 103, 'marks': 96}


