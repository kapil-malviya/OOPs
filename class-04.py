

class Student :
	def __init__(self) :
		self.name = 'kapil'
		self.rollno = 808
		self.marks = 80

	def talk(self):
		print('hello folks, my name is ',self.name)
		print('my roll roll no is ',self.rollno)
		print('and i got ',self.marks,'marks')

s = Student()
s.talk()
print(s.name, s.rollno, s.marks)           # =>>   kapil 808 80
