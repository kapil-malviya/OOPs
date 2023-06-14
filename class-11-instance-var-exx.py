##  another example of instance variable : 

class SE :

	def __init__(self, name, age, tech) :
		self.name = name
		self.age = age
		self.tech = tech

s1 = SE('kapil-8', 88, 'devops')
s2 = SE('kapil-88', 80, 'PM')

s1.gf = 'sonam bajwa'
s1.gf2 = 'kylie jenner'
s2.brand = 'JW'
s2.brand2 = 'JD'

print(s1.__dict__)

# output =>>  {'name': 'kapil-8', 'age': 88, 'tech': 'devops', 'gf': 'sonam bajwa', 'gf2': 'kylie jenner'}


print(s2.__dict__)

# output =>>  {'name': 'kapil-88', 'age': 80, 'tech': 'PM', 'brand': 'JW', 'brand2': 'JD'}


