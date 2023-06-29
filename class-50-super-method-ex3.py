'''
# super() method : another example ;


-> parent class instance variable can't be accessed through super() method

-> instance methods, constructor... is allowed to access but not instance variable

-> parent class instance variable is available to the child class, but can't be 
	accessed through super() method

-> instance class variable should be accesssed through ' self.x ' onlyy



class B :
	a = 8888
	def m1(self) :
		self.a = 80 

class P(B) :
	def __init__(self) :
#		super().m1()
		self.m1()
		print(super().a)
		print(self.a)

o = P()



output =>> 

8888
80              

'''


class P :
	a = 999
	def __init__(self) :
		self.b = 80 

	def m1(self) :
		self.b = 333

class C(P) :
	a = 888
	def __init__(self) :
		self.b = 90
		print('before executing parent class constructor : ',self.b)  # 90
		super().__init__()
		print(C.a)                   # 888
		print(self.a)                # 888
		print(super().a)             # 999

		print('after executing parent class constructor : ',self.b)   # 80

		super().m1()
		print('after calling method m1 : ', self.b)    # 333

o = C()