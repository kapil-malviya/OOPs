
#  Overloading > and <= operators for Student class objects:
'''

class Student :
	def __init__(self, name, marks) :
		self.name = name
		self.marks = marks

	def __gt__(self, other) :
		return self.marks > other.marks

	def __le__(self, other) :
		return self.marks <= other.marks

#print('10 > 20 = ', 10>20)

s1 = Student('kapil-8', 80)
s2 = Student('kapil-88', 880)

print('s1 > s2 = ', s1 > s2)          # False
print('s1 < s2 = ', s1 < s2)          # True
print('s1 <= s2 = ', s1 <= s2)        # True
print('s1 >= s2 = ', s1 >= s2)        # False           '''




## overload ( * ) multiplication operator to work on Employee objects :


class Employee :
	def __init__(self, name, salary) :
		self.name = name 
		self.salary = salary

	def __mul__(self, other) :
		return self.salary * other.days

class TimeSheet :
	def __init__(self, name, days) :
		self.name = name
		self.days = days


e = Employee('kapil', 888)
t = TimeSheet('kapil', 18)

print('Current month salary : ', e * t)   # total salary : 15984
# print('Current month salary : ', t * e)   # TypeError