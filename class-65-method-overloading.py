'''
# How we can handle overloaded method requirements in Python :

-> Most of the times, if method with variable number of arguments required then we can handle
	with default arguments or with variable number of argument methods.

=>> Program with Default Arguments :





class Test :
	def sum(self, a=None, b=None, c=None) :       # None is more meaningfull than 0(zero)
		if a!=None and b!=None and c!=None :
			print('the sum of a, b & c is : ', a+b+c)
		elif a!=None and b!=None :
			print('the sum of a & b : ', a+b)
		else :
			print('please provide 2 or 3 values only')

t = Test()
t.sum(18, 28)
t.sum(18, 28, 88)
t.sum()

  ---> 
the sum of a & b :  46
the sum of a, b & c is :  134
please provide 2 or 3 values only                 '''





###  Program with Variable Number of Arguments :


class Test :
	def sum(self, *n) :
		total=0
		for x in n :
			total = total + x
		print('The Sum : ' , total)

t = Test()
t.sum(10, 20)
t.sum(10, 20, 30)
t.sum(10)
t.sum() 



'''  ----> 

The Sum :  30
The Sum :  60
The Sum :  10
The Sum :  0                  '''