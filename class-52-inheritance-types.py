'''

Inheritance types : python supported inheritance types ;

-> single
-> multi level
-> hierarchical
-> multiple
-> cyclic : only cyclic inheritance not supported in python 
-> hybrid



##  Single Inheritance : 

->> the conceptof inheriting members of one class to another class
->> single parent class to single child class

'''


class P :
	def m1(self) :
		print('parent method')

class C(P) :
	def m2(self) :
		print('child method')


c = C()
c.m1()
c.m2()

