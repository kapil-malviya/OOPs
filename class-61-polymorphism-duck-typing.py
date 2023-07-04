'''
	hasattr(obj,'attributename')

attributename can be method name or variable name


=>> demo program with hasattr() function :      

'''


class Duck :
	def talk(self) :
		print('quack quack quack...')

class Dog :
	def bark(self) :
		print('bhow bhaw...')

class Cat :
	def talk(self) :
		print('meow meow...')

class Goat :
	def talk(self) :
		print('myaah myaah...')

l = [Duck(), Dog(), Cat(), Goat()]

for obj in l :
	if hasattr(obj, 'talk') :
		obj.talk()
	elif hasattr(obj, 'bark') :
		obj.bark()

'''

now we won't get the attribute error,    '''