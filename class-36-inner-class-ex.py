'''

Inner classes/Nested class : examples ;

-> Without existing outer class object there is no chance of existing 
	inner class object. Hence inner class object is always associated 
	with outer class object.


## Accessing inner class : various ways ;

o = Outer()
i = o.Inner()
i.m1()

--------------------

i = Outer().Inner()
i.m1()

--------------------

Outer().Inner().m1()


'''


class Person :
	def __init__(self) :
		print('Person Class Constructor')
		self.name = 'kapil'
		self.db = self.Dob()

	def display(self) :
		print('name : ', self.name)

	class Dob :
		def __init__(self) :
			print('Dob Class Constructor')
			self.dd = 8
			self.mm = 5
			self.yy = 1888

		def display(self) :
			print('Dob : {}/{}/{}'.format(self.dd, self.mm, self.yy))

p = Person()               # while initialisation db object also created ;
p.display()
p.db.display()