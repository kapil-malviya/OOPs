# Constructor Overloading :

'''

-> Constructor overloading is not possible in Python
-> If we define multiple constructors then the last constructor will be considered
-> In python only Operator Overloading is supported





class Test :
	def __init__(self) :
		print('no argument constructor')

	def __init__(self, a) :
		print('one argument constructor')

	def __init__(self, a, b) :
		print('two argument constructor')

# t1 = Test()      TypeError:
# t1 = Test(8)     TypeError:
t1 = Test(8, 88)     #  two argument constructor
'''




# based on our requirement we can declare constructor with default arguments and variable number of arguments :


class Test :
	def __init__(self, *n) :
		print('constructor with variable no. of argument...')

t1 = Test()
t2 = Test(80)
t2 = Test(80, 888)
t2 = Test(80, 888, 888)


'''
constructor with variable no. of argument...
constructor with variable no. of argument...
constructor with variable no. of argument...
constructor with variable no. of argument...               '''