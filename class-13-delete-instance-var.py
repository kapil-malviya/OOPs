"""   delete instance variable 

How to delete instance variable from the object :

	-> Within a class we can delete instance variable as follows
		del self.variableName

	-> From outside of class we can delete instance variables as follows
		del objectreference.variableName

"""


class Test :

	def __init__(self) :
		self.a = 18
		self.b = 28
		self.c = 38
		self.d = 48

t1 = Test()
t2 = Test()

print('t1 : ', t1.__dict__)
print('t2 : ', t2.__dict__)

"""  output =>>
t1 :  {'a': 18, 'b': 28, 'c': 38, 'd': 48}
t2 :  {'a': 18, 'b': 28, 'c': 38, 'd': 48}    """

del t1.a 
print('t1 : ', t1.__dict__)
print('t2 : ', t2.__dict__)


#  The instance variables which are deleted from one object, will not be deleted from other objects.


"""  output =>>
t1 :  {'b': 28, 'c': 38, 'd': 48}
t2 :  {'a': 18, 'b': 28, 'c': 38, 'd': 48}     """

del t2.d 
print('t1 : ', t1.__dict__)
print('t2 : ', t2.__dict__)

"""  output =>>
t1 :  {'b': 28, 'c': 38, 'd': 48}
t2 :  {'a': 18, 'b': 28, 'c': 38}             """

