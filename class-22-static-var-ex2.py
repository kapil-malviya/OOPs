"""
various examples for static variable :

"""



class Test :
	x = 88
	def __init__(self) :
		self.y = 888

t1 = Test()
t2 = Test()

t1.x = t1.x+1        # 89
t2.y = t2.y+1        # 889

print('t1 : ', t1.x, t1.y)    #  89  888    < here both are instance var.
print('t2 : ', t2.x, t2.y)    #  88  889
print('Test : ', Test.x)      #  88



print(t1.__dict__)    #  {'y': 888, 'x': 89}     both instance var. for object t1
print(t2.__dict__)    #  {'y': 889}              y is instance var. & x is still static var. for ovject t2