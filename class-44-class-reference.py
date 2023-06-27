## one way :

class X :
	def m1() :
	def m2() :
	def m3() :
	def m4() :

class Y :
	x = X()
	x.m1()
	x.m2()
	x.m3()
	x.m4()

# class Y  has-a X reference


## another way : 

class X :
	def m1() :
	def m2() :
	def m3() :
	def m4() :

class Y(X) :

y = Y()
y.m1()
y.m2()
y.m3()
y.m4()


'''
class Y(X) :
class childclass(parentclass) : 


'''