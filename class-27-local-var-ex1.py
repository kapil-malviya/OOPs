"""
Local variable : another example ;


-> Local variables of a method cannot be accessed from outside of method...




class Test :
	def m1() :
		a = 80
		print(a)
	def m2() :
		b = 83
		print(b)
	#	print(a)   =>  NameError: name 'a' is not defined  => can not be accessed from outside of method

t = Test
t.m1()       #  80
t.m2()       #  83



"""


class Test :

	def m1() :
		a = 88
		print(a)

	def m2() :
		b = 888
		a = 999
		print(a)
		print(b)

Test.m1()       # 88

Test.m2()       # 999 \n  888