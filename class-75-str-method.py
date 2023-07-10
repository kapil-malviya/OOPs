###   __str__() method :
'''

-> whenever we are printing any object reference, internally __str__() method will
	will be called which returns the following format : 

	print(object)
	<__main__.Student object at 0x00000251C5AE7390>

-> to return meaningful string representation we have to override __str__() method.

'''



class Student :
	def __init__(self, name, rollno) :
		self.name = name
		self.rollno = rollno

	def __str__(self) :
		return 'this is student with name : {} & rollno : {}'.format(self.name, self.rollno)

s1 = Student('harsh', 101)
s2 = Student('anna', 102)

print(s1)
print(s2)


'''
=>> output without overriding __str__() method :

<__main__.Student object at 0x000001A87EB57850>
<__main__.Student object at 0x000001A87EB575D0>


=>> output with overriding __str__() method : 

this is student with name : harsh & rollno : 101
this is student with name : anna & rollno : 102

'''