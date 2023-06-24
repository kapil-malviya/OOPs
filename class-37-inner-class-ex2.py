'''

Inner classes/Nested class : 

'''

class Human :
	def __init__(self) :
		self.name = 'kapil'
		self.head = self.Head()
		self.brain = self.Brain()

	def display (self) :
		print('heloo', self.name)

	class Head :
		def talk (self) :
			print('talking...')

	class Brain :
		def think(self) :
			print('thinking...')

h = Human()
h.display()
h.head.talk()
h.brain.think()