'''
##  Method Overloading :

-> If 2 methods having same name but different type of arguments then those methods are 
	said to be overloaded methods

Eg : 
	m1(int a)
	m1(double d)


-> But in Python Method overloading is not possible.

-> If we are trying to declare multiple methods with same name and different number of 
	arguments then Python will always consider only last method.

'''

#  python will consider only last method.


class Test :
	def m1(self) :
		print('no-arg method')

	def m1(self, a) :
		print('one-arg method')

	def m1(self, a, b) :
		print('two-arg method')

t = Test()
# t.m1()
# t.m1(10)
t.m1(10,20)      #  two-arg method


# then, how we'll handle overloaded method requirements in Python ;