'''
super() method : 


-> In case of variables, super method is allowed to access only class level 
	variable and not instance variables.,

'''

class B :
	x = 888
	def __init__(self) :
		self.x = 80
		self.y = 88
		print('class constructor')

class W(B) :
	def __init__(self) :
#		self.y = 90           # here y value won't be replaced with 90, bcoz we're calling constructor later
		super().__init__()
		self.y = 90           # here y value replaced with 90       
		print(super().x)
		print(self.x)
		print(self.__dict__)

o = W()


'''  =>> 

class constructor
888
80
{'x': 80, 'y': 90}                              '''