'''
	Instance Variable vs Static Variable :

In case of instance variables for every object a seperate copy will be created, 
but in case of static variables for total class only one copy will be created 
and shared by every object of that class.,

'''


class Test :
	x = 80
	def __init__(self) :
		self.y = 88

t1 = Test()
t2 = Test()

print('t1 : ', t1.x, t1.y)      # 80  88
print('t2 : ', t2.x, t2.y)      # 80  88

"""
Test.x = 888          # perfofrming change to the static variable
t1.y = 999

print('t1 : ', t1.x, t1.y)      # 888  999
print('t2 : ', t2.x, t2.y)      # 888  88

"""

t1.x = 888       #  here we're not modifying static variable x, but we're adding
t2.x = 999       #    instance variable x to the t1 and t2 object

print('t1 : ', t1.x, t1.y)      # 888  88
print('t2 : ', t2.x, t2.y)      # 999  88

print(t1.__dict__)        # {'y': 88, 'x': 888}    instance variables of t1 object
print(t2.__dict__)        # {'y': 88, 'x': 999}    instance variables of t2 object