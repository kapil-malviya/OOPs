''' 
		(Duck Typing Principle of Python)

###  Polymorphism :

-> Poly means many, Morphs means forms
-> Polymorphism means 'Many Forms'

-> Eg 1 : Yourself is best example of polymorphism.In front of Your parents 
			you will have one type of behaviour and with friends another type 
			of behaviour. Same person but different behaviours at different places, 
			which is nothing but polymorphism.
-> Eg 2 : + operator acts as concatenation and arithmetic addition
-> Eg 3 : * operator acts as multiplication and repetition operator
-> Eg 4 : The Same method with different implementations in Parent class and child
			classes. (overriding)

#=> Related to polymorphism the following 4 topics are important

-> Duck Typing Philosophy of Python
-> Overloading
	-> Operator Overloading
	-> Method Overloading
	-> Constructor Overloading
-> Overriding
	-> Method overriding
	-> Constructor overriding


##  Duck Typing Philosophy of Python :

-> In Python we cannot specify the type explicitly. Based on provided value 
	at runtime the type will be considered automatically. Hence Python is 
	considered as Dynamically Typed Programming Language.

	def f1(obj) :
		obj.talk()

-> What is the type of obj? We cannot decide at the beginning. At runtime 
	we can pass any type. Then how we can decide the type?

-> At runtime if 'it walks like a duck and talks like a duck, it must be duck'. 
	Python follows this principle. This is called Duck Typing Philosophy of Python.

'''


class Duck :
	def talk(self) :
		print('quack quack quack...')

class Dog :
	def talk(self) :
		print('bhow bhaw...')

class Cat :
	def talk(self) :
		print('meow meow...')

class Goat :
	def talk(self) :
		print('myaah myaah...')

l = [Duck(), Dog(), Cat(), Goat()]

for obj in l :
	obj.talk()


'''
The problem in this approach is if obj does not contain talk() method then we will get
AttributeError

But we can solve this problem by using hasattr() function.

	hasattr(obj,'attributename')

attributename can be method name or variable name

'''