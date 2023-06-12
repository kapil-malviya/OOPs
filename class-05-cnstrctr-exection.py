#  Program to demonstrate constructor will execute only once per object =>>

class Test:
	def __init__(self):
		print("Constructor exeuction...")

	def m1(self):
		print("Method execution...")

t1=Test()
t2=Test()
t2.m1()
t3=Test()
t1.m1() 


"""
result =>>

Constructor exeuction...
Constructor exeuction...
Method execution...
Constructor exeuction...
Method execution...

"""