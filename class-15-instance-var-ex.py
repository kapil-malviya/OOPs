"""

Instance Variable : 

	If we change the values of instance variables of one object then those 
	changes won't be reflected to the remaining objects, because for every 
	object we have separate copy of instance variables available,,

"""

class Test :

	def __init__(self) :
		self.a = 80
		self.b = 88

t1 = Test()
t1.a = 888
t1.b = 800

t2 = Test()
print('t1 : ', t1.a, t1.b)
print('t2 : ', t2.a, t2.b)


""" output =>>

t1 :  888 800
t2 :  80 88               """