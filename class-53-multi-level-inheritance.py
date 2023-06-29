'''

## Multi level Inheritance : 

->> the concept of inheriting properties from property of multiple classes
	to the single class with the concept of one after another

->> for example : child --> father --> grand father --> great grand father --> and so on..


'''


class GF :
	def m1(self) :
		print('grand phather class')

class F(GF) :
	def m2(self) :
		print('phather class')

class C(F) :
	def m3(self) :
		print('childd class')

c = C()
c.m1()
c.m2()
c.m3()


'''  =>> 

grand phather class
phather class
childd class                '''