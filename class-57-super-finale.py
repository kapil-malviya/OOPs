

class P :
	a = 18 
	def __init__(self) :
#		self.b = 20
		print('constructor')

	def m1(self) :
		print('instance method')

	@classmethod
	def m2(cls) :
		print('class method')

	@staticmethod
	def m3() :
		print('static method')

'''
class C(P) :
#	a = 28
	def m1(self) :
#		print(super().b)     # AttributeError: 'super' object has no attribute 'b' : won't access instance variable
#		print(self.a)        # 28
		print(super().a)     # 18
		super().__init__()
		super().m1()
		super().m2()
		super().m3()

c = C()
c.m1()



--------->> output : 
constructor
18
constructor
instance method
class method
static method          
---------------------

###  Inside child class : 
1. Instance method : no restriction to use super()


class C(P) :
	def __init__(self) :
		print(super().a)     # 18
		super().__init__()
		super().m1()
		super().m2()
		super().m3()	
c = C()



--------->> output : 

18
constructor
instance method
class method
static method
---------------------


2. Constructor : no restriction to use super().;                          '''



'''

class C(P) :
	@classmethod
	def m1(cls) :
		print(super().a)     # 18
#		super().__init__()
#		super().m1()
		super().m2()
		super().m3()	
c = C()
c.m1()



--------->> output : 

18
class method
static method
---------------------



3. Classmethod : 
		-> from classmethod of child class we can not call parent class constructor by using super()
		-> from classmethod of child class we can not call parent class instance method by using super()    '''




class C(P) :
	@staticmethod
	def m1() :
		pass
#		print(super().a)
#		super().__init__()
#		super().m1()
#		super().m2()
#		super().m3()	


c = C()




'''

4. Staticmethod : 
		-> from static method of child class we can not use the super method ;      


'''

