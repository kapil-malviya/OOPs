# object creation

class Student :          # by convention Upper case for the first letter of class     
	def __init__(self, name, rollno, marks):
		self.name = name                     # for initialisation of object constructor (__init__) must require
		self.rollno = rollno                 # initialisation of object means -> to provide values for the instance variable
		self.marks = marks                   # 

s1 = Student('kapil', 1008, 88)               # object creation
print(s1.name)
print(s1.name, s1.rollno, s1.marks)           # accessing that object

s2 = Student('kylie', 1009, 90)                
print(s2.name, s2.rollno, s2.marks)

print(s1)        #  =>>   <__main__.Student object at 0x000001BAC3977690>


#  self  =>> it is not a keyword nor reserved word
#  within the class, instance variable we have to access by using the self keyword


"""

	def __init__(self, name, rollno, marks):      =>> here  name, rollno, marks => are normal variable  
		self.name = name                         | self.name     = these are instance variable
		self.rollno = rollno                     | self.rollno   =    --------------------
		self.marks = marks                       | self.marks    =         ----------

		==>>  name, rollno, marks => object related instance variable







class Student :          
	def __init__(self, x, xx, xxx):
		self.name = x                 
		self.rollno = xx             
		self.marks = xxx         

s1 = Student('kapil', 1008, 88)             
print(s1.name, s1.rollno, s1.marks)         

s2 = Student('kylie', 1009, 90)             
print(s2.name, s2.rollno, s2.marks)


"""
