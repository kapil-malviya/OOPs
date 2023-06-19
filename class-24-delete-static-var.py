"""

Delete static variables :

- We can delete static variables from anywhere by using the following syntax :
	
	del classname.variablename

- & inside classmethod we can also use cls variable : 
	
	del cls.variablename                                                                                          




class Test :
	x = 8
	@classmethod
	def m1(cls) :
		del cls.x

print(Test.__dict__)        # {.., 'x': 8, ..}

Test.m1()
print(Test.__dict__)       # no static var. present with name 'x'


"""


class Test :
	a = 8
#	def __init__(self) :
	#	del self.a            can't delete static var. via self here 


print(Test.__dict__)

# del t.a      can't delete static var. via object reference        

del Test.a
print(Test.__dict__)