'''
=> Overriding
	-> Method overriding
	-> Constructor overriding

-> Overriding concept applicable for both methods and constructors.


##  Method Overriding :

-> Whatever members available in the parent class are bydefault available to the 
	child class through inheritance. If the child class not satisfied with parent 
	class implementation, then child class is allowed to redefine that method in 
	the child class based on its requirement. This concept is called overriding.
'''


class P :
	def property(self) :
		print('cash + land + gold + semen')

	def marry(self) :
		print('katrina kaif')

class C(P) :
	def marry(self) :
		super().marry()      
# From Overriding method of child class, we can call parent class method also by super() method.
		print('sonam bajwa')

c = C()
c.property()
c.marry()


'''
----------->> output : 

cash + land + gold + semen
katrina kaif
sonam bajwa                  '''