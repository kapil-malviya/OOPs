#  doc string and help()



class Student : 
	''' This is Student class with the required data '''
	def __init__(self, x, xx, xxx) :
		self.name = x                 
		self.rollno = xx             
		self.marks = xxx         

	def display(self) :
		print('Students Name : {}, RollNo : {}, Marks : {}'.format(self.name, self.rollno, self.marks))

s = Student('kapil', 1008, 88)             
s.display()
print()  
print('via class name : ',Student.__doc__)    
print('via object reference : ',s.__doc__)
print()
help(Student)


"""
	Documentation string represents description of the class. Within the class doc string is always optional. 
	We can get doc string by using the following 2 ways =>>
	
	1. print(classname.__doc__)
	2. help(classname)




## returns ==>> 

Students Name : kapil, RollNo : 1008, Marks : 88

 This is Student class with the required data

Help on class Student in module __main__:

class Student(builtins.object)
 |  Student(x, xx, xxx)
 |
 |  This is Student class with the required data
 |
 |  Methods defined here:
 |
 |  __init__(self, x, xx, xxx)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  display(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
-- More  --


"""