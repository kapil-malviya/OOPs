'''

##  Multiple Inheritance  :

-> the concept of inheriting the properties from multiple classes into a single
	class at a time, is known as multiple inheritance. 

-> multiple parent class to the single child class,              ''' 


'''


class P1 :
	def m1(self) :
		print("Parent1 Method")

class P2 :
	def m2(self) :
		print("Parent2 Method")

class C(P1, P2) :
	def m3(self) :
		print("Child Method")

c=C()
c.m1()
c.m2()
c.m3() 


 ------->> output :

Parent1 Method
Parent2 Method
Child Method                      
---------------------



-> If the same method is inherited from both parent classes, then Python 
	will always consider the order of Parent classes in the declaration 
	of the child class.

class C(P1,P2): ===>P1 method will be considered
class C(P2,P1): ===>P2 method will be considered          


class P1 : 
	def m1(self) :
		print("Parent1 Method")

class P2 :
	def m1(self) :
		print("Parent2 Method")

#class C(P1, P2) :
class C(P2, P1) :           # first consider P2 then P1
	def m2(self) :
		print("Child Method")

c=C()
c.m1()
c.m2() 

# if child class also has m1 method, then priority will first come to the child class m1 method


------->> output :

Parent2 Method
Child Method                   '''