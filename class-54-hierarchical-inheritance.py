'''

## Hierarchical Inheritance : 

->> one to many : single parent class to the multiple child class,


'''

class P() :
	def m1(self) :
		print('parent class')


class C1(P) :
	def m2(self) :
		print('C1 child class')


class C2(P) :
	def m3(self) :
		print('C2 child class')


c1 = C1()
c1.m1()
c1.m2()

print()

c2 = C2()
c2.m1()
c2.m3()


''' =>> 

parent class
C1 child class

parent class
C2 child class                   '''