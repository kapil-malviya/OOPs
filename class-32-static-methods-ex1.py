'''

##  Static Methods :

-> In general these methods are general utility methods.

-> Inside these methods we won't use any instance or class variables.

-> Here we won't provide self or cls arguments at the time of declaration.

-> We can declare static method explicitly by using @staticmethod decorator.

-> We can access static method by using classname or object reference.

'''


class Math :

	@staticmethod
	def add(x,y) :
		print('the sum : ', x+y)

	@staticmethod
	def product(x,y) :
		print('the product : ', x*y)

	@staticmethod
	def average(x,y) :
		print('the average : ', (x+y)/2)

# here object is not required because we're not calling any instance variable & not creating object

Math.add(80,83)
Math.product(80,83)
Math.average(80,83)

"""  output :

the sum :  163
the product :  6640
the average :  81.5                         """