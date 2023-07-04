'''  Operator overloading

-> Overloading
	-> Operator Overloading
	-> Method Overloading
	-> Constructor Overloading

#  Overloading :
		-> We can use same operator or methods for different purposes.

-> Eg 1 :  + operator can be used for Arithmetic addition and String concatenation
			print(10+20)   # 30
			print('durga'+'soft')  # durgasoft

-> Eg 2 :  * operator can be used for multiplication and string repetition purposes.
			print(10*20)   # 200
			print('durga'*3)   # durgadurgadurga

-> Eg 3 :  We can use deposit() method to deposit cash or cheque or dd
			deposit(cash)
			deposit(cheque)
			deposit(dd)


##  Operator Overloading :

	-> We can use the same operator for multiple purposes, which is nothing but operator overloading.
	-> Python supports operator overloading.



# Demo program to use + operator for our class objects :

class Book :
	def __init__(self, pages) :
		self.pages=pages

b1=Book(100)
b2=Book(200)
print(b1+b2)


----------------->

Traceback (most recent call last):
 File "test.py", line 7, in <module>
 print(b1+b2)
TypeError: unsupported operand type(s) for +: 'Book' and 'Book'
----------------------<


-> We can overload + operator to work with Book objects also. i.e Python 
	supports Operator Overloading.

-> For every operator Magic Methods are available. To overload any operator 
	we have to override that Method in our class.

=>>
	Internally + operator is implemented by using __add__() method.
	This method is called magic method for + operator. 
	We have to override this method in our class.

'''


class Book :
	def __init__(self, pages) :
		self.pages = pages

	def __add__(self, other) :
		return self.pages + other.pages

b1 = Book(80)
b2 = Book(88)
print('the total no. of pages : ', b1 + b2)   # 168


b1 = Book('80')
b2 = Book('88')
print('the total no. of pages : ', b1 + b2)   # 8088


"""

The following is the list of operators and corresponding magic methods : 

+ ---> object.__add__(self,other)
- ---> object.__sub__(self,other)
* ---> object.__mul__(self,other)
/ ---> object.__div__(self,other)
// ---> object.__floordiv__(self,other)
% ---> object.__mod__(self,other)
** ---> object.__pow__(self,other)
+= ---> object.__iadd__(self,other)
-= ---> object.__isub__(self,other)
*= ---> object.__imul__(self,other)
/= ---> object.__idiv__(self,other)
//= ---> object.__ifloordiv__(self,other)
%= ---> object.__imod__(self,other)
**= ---> object.__ipow__(self,other)
< ---> object.__lt__(self,other)
<= ---> object.__le__(self,other)
> ---> object.__gt__(self,other)
>= ---> object.__ge__(self,other)
== ---> object.__eq__(self,other)
!= ---> object.__ne__(self,other)


"""