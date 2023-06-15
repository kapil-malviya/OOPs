###  Static variables :

"""

If the value of a variable is not varied from object to object, such type of 
variables we have to declare with in the class directly but outside of methods.
Such type of variables are called Static variables..,

For total class only one copy of static variable will be created and shared by 
all objects of that class,

We can access static variables either by class name or by object reference. But 
recommended to use class name.,

"""



class Test :
	x = 88
	def __init__(self) :
		self.y = 800

t = Test()
print(t.x, t.y)
print(Test.x, t.y)

""" output =>>

88 800
88 800             """
