"""

Where we can modify the value of static variable :

	Anywhere either within the class or outside of class we can modify 
	by using classname., but inside class method, by using cls variable...             """


class Test :
	a = 8
	def __init__(self) :
		self.b = 18

t1 = Test()
t2 = Test()

"""
t1.a = 888   # here it's not modifying static var.(a) but creating instance var. (a) for object t1
t1.b = 999   # here it's modifying instance var. (b) by 999 from 18

print(t2.a, t2.b)     #    8   18
print(t1.a, t1.b)     #  888  999

print(t1.__dict__)    #  {'b': 999, 'a': 888}       # showing instance var. of object t1
print(t2.__dict__)    #  {'b': 18}                  # showing instance var. of object t2

"""

## use class name instead of object reference for modifying the static variable.. :

print(Test.__dict__)   # =>   {... 'a': 8, ...}

Test.a = 888
t1.b = 999

print(t2.a, t2.b)     #  888   18
print(t1.a, t1.b)     #  888  999

print(t1.__dict__)    #  {'b': 999}       # showing instance var. of object t1
print(t2.__dict__)    #  {'b': 18}        # showing instance var. of object t2

print(Test.__dict__)   # =>   {... 'a': 888, ...}


"""

If we change the value of static variable by using either self or object reference 
variable, then the value of static variable won't be changed, just a new instance 
variable with that name will be added to that particular object...                      """